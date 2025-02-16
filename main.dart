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
  @override
  Widget build(BuildContext context) {
    if (_controller == null || !_controller!.value.isInitialized) {
      return Center(child: CircularProgressIndicator());
    }

    return Scaffold(
      body: Stack(
        children:[
          CameraPreview(_controller!),
          Positioned(
            top: 50,
            left: 20,
            right: 20,
            child: Row(
              mainAxisAlignment: MainAxisAlignment.spaceBetween,
              children: [
                IconButton(
                  icon: Icon(isFlashOn ? Icons.flash_on : Icons.flash_off, color: Colors.white),
                  onPressed: () {
                    setState(() {
                      isFlashOn = !isFlashOn;
                      _controller!.setFlashMode(
                        isFlashOn ? FlashMode.torch : FlashMode.off,
                      );
                    });
                  },
                ),
                Icon(Icons.wb_sunny, color: Colors.white), // Placeholder for Brightness Control
                IconButton(
                  icon: Icon(Icons.language, color: Colors.white),
                  onPressed: () {
                  },
                ),
              ],
            ),
          ),
  
