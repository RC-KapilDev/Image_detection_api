from flask import Flask, request, jsonify
import your_object_detection_module  # Import your object detection module

app = Flask(_name_)

@app.route('/api/object-detection', methods=['GET'])
def object_detection():
    image_url = request.args.get('image_url')
    
    if not image_url:
        return jsonify({'error': 'Image URL not provided'}), 400
    
    # Perform object detection using your model
    detection_results = your_object_detection_module.detect_objects(image_url)
    
    # Return the detection results as JSON
    return jsonify(detection_results)

if _name_ == '_main_':
    app.run(debug=True)