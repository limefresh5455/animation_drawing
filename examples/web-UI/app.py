from flask import Flask ,render_template,request
import os
import subprocess
# from animated_drawings import render

app = Flask(__name__)

@app.route("/",methods=["POST","GET"])
def fun():
    
    if request.method == 'POST':
      f = request.files['file']
      filename = f.filename
      # filename = "garlic_out"
      print(filename)
      destination_dir = 'C:/Users/Linuxbean/AnimatedDrawings-main/examples/drawings'
      if not os.path.exists(destination_dir):
          os.makedirs(destination_dir)
      file_path = os.path.join(destination_dir, f.filename)
      f.save(file_path) 
      cmd =  f"cd .. ; python image_to_animation.py drawings/{filename} {filename}/"
      #   cmd = f"cd .. ; python fix_annotations.py {filename}/"
    #   cmd = "cd .. ; pwd"
      print(cmd)
      k = run(cmd)
      print("Processing")
      # return f"processing your image {k}"
      return render_template("video.html",filename=filename)
    return render_template('index.html')

def run(cmd):
    print("running")
    completed = subprocess.run(["powershell", "-Command", cmd], capture_output=True)
    print(completed)
    return completed.stdout.decode("utf-8")


if __name__ == "__main__" :
    app.run()


