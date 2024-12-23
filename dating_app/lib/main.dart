import 'package:flutter/material.dart';
import 'package:http/http.dart' as http;
import 'dart:convert';

void main() {
  runApp(DatingApp());
}

class DatingApp extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'Dating App',
      home: UserRegistrationScreen(),
    );
  }
}

class UserRegistrationScreen extends StatefulWidget {
  @override
  _UserRegistrationScreenState createState() => _UserRegistrationScreenState();
}

class _UserRegistrationScreenState extends State<UserRegistrationScreen> {
  final TextEditingController nameController = TextEditingController();
  final TextEditingController interestsController = TextEditingController();
  final TextEditingController affiliationsController = TextEditingController();
  final TextEditingController demographicsController = TextEditingController();

  Future<void> registerUser() async {
    final url = Uri.parse('http://127.0.0.1:5000/add_user');
    final response = await http.post(
      url,
      headers: {'Content-Type': 'application/json'},
      body: jsonEncode({
        'name': nameController.text,
        'interests': interestsController.text,
        'affiliations': affiliationsController.text,
        'demographics': demographicsController.text,
      }),
    );

    if (response.statusCode == 200) {
      final data = jsonDecode(response.body);
      Navigator.push(
        context,
        MaterialPageRoute(
          builder: (context) => MatchScreen(userId: data['user_id']),
        ),
      );
    } else {
      ScaffoldMessenger.of(context).showSnackBar(
        SnackBar(content: Text('Failed to register user')),
      );
    }
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: Text('User Registration')),
      body: Padding(
        padding: const EdgeInsets.all(16.0),
        child: Column(
          children: [
            TextField(
              controller: nameController,
              decoration: InputDecoration(labelText: 'Name'),
            ),
            TextField(
              controller: interestsController,
              decoration: InputDecoration(labelText: 'Interests'),
            ),
            TextField(
              controller: affiliationsController,
              decoration: InputDecoration(labelText: 'Affiliations'),
            ),
            TextField(
              controller: demographicsController,
              decoration: InputDecoration(labelText: 'Demographics (JSON)'),
            ),
            SizedBox(height: 20),
            ElevatedButton(
              onPressed: registerUser,
              child: Text('Register'),
            ),
          ],
        ),
      ),
    );
  }
}
