import 'package:flutter/material.dart';
import 'package:camera/camera.dart';

void main() async {
  WidgetsFlutterBinding.ensureInitialized();
  final cameras = await availableCameras();
  runApp(CameraApp(cameras: cameras));
}

class CameraApp extends StatelessWidget {
  final List<CameraDescription> cameras;
  CameraApp({required this.cameras});

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      debugShowCheckedModeBanner: false,
      home: CameraScreen(cameras: cameras),
    );
  }
}
class CameraScreen extends StatefulWidget {
  final List<CameraDescription> cameras;
  CameraScreen({required this.cameras});

  @override
  _CameraScreenState createState() => _CameraScreenState();
}

class _CameraScreenState extends State<CameraScreen> {
  CameraController? _controller;
  bool isRearCamera = true;
  bool isFlashOn = false;

  @override
  void initState() {
    super.initState();
    _initializeCamera(isRearCamera);
  }

  void _initializeCamera(bool rear) {
    _controller = CameraController(
      rear ? widget.cameras[0] : widget.cameras[1],
      ResolutionPreset.high,
    );

    _controller!.initialize().then((_) {
      if (!mounted) return;
      setState(() {});
    }).catchError((e) {
      print('Camera Error: $e');
    });
  }

  @override
  void dispose() {
    _controller?.dispose();
    super.dispose();
  }
