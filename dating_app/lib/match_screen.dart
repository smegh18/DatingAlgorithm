import 'package:flutter/material.dart';
import 'package:http/http.dart' as http;
import 'dart:convert';

class MatchScreen extends StatelessWidget {
  final int userId;

  MatchScreen({required this.userId});

  Future<List<dynamic>> fetchMatches() async {
    final url = Uri.parse('http://127.0.0.1:5000/find_matches');
    final response = await http.post(
      url,
      headers: {'Content-Type': 'application/json'},
      body: jsonEncode({'user_id': userId}),
    );

    if (response.statusCode == 200) {
      return jsonDecode(response.body);
    } else {
      throw Exception('Failed to fetch matches');
    }
  }

  Future<void> sendReaction(int matchId, String reaction) async {
    final url = Uri.parse('http://127.0.0.1:5000/react_to_match');
    final response = await http.post(
      url,
      headers: {'Content-Type': 'application/json'},
      body: jsonEncode({'user_id': userId, 'match_id': matchId, 'reaction': reaction}),
    );

    if (response.statusCode == 200) {
      print('Reaction recorded');
    } else {
      print('Failed to send reaction');
    }
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: Text('Matches')),
      body: FutureBuilder<List<dynamic>>(
        future: fetchMatches(),
        builder: (context, snapshot) {
          if (snapshot.connectionState == ConnectionState.waiting) {
            return Center(child: CircularProgressIndicator());
          } else if (snapshot.hasError) {
            return Center(child: Text('Error: ${snapshot.error}'));
          } else {
            final matches = snapshot.data!;
            return ListView.builder(
              itemCount: matches.length,
              itemBuilder: (context, index) {
                final match = matches[index];
                return ListTile(
                  title: Text(match['name']),
                  subtitle: Text('Interests: ${match['interests']}'),
                  trailing: Row(
                    mainAxisSize: MainAxisSize.min,
                    children: [
                      IconButton(
                        icon: Icon(Icons.thumb_up, color: Colors.green),
                        onPressed: () => sendReaction(match['id'], 'like'),
                      ),
                      IconButton(
                        icon: Icon(Icons.thumb_down, color: Colors.red),
                        onPressed: () => sendReaction(match['id'], 'dislike'),
                      ),
                    ],
                  ),
                );
              },
            );
          }
        },
      ),
    );
  }
}
