<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <!-- <title>Iris Classification - README</title> -->
</head>
<body>

<h1>🌸 Iris Species Classification Web Application</h1>

<p>A <strong>Flask-based web application</strong> that classifies Iris flower species using <strong>K-Nearest Neighbors (KNN)</strong> and <strong>Naive Bayes</strong> machine learning algorithms. The application provides an interactive dashboard where users can input flower measurements and get real-time predictions along with model performance metrics.</p>

<hr>

<h2>📋 Table of Contents</h2>
<ul>
    <li><a href="#features">Features</a></li>
    <li><a href="#live-demo">Live Demo</a></li>
    <li><a href="#screenshots">Screenshots</a></li>
    <li><a href="#tech-stack">Tech Stack</a></li>
    <li><a href="#dataset">Dataset</a></li>
    <li><a href="#model-performance">Model Performance</a></li>
    <li><a href="#installation">Installation</a></li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#project-structure">Project Structure</a></li>
    <li><a href="#deployment">Deployment</a></li>
    <li><a href="#troubleshooting">Troubleshooting</a></li>
    <li><a href="#future-enhancements">Future Enhancements</a></li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#license">License</a></li>
</ul>

<hr>

<h2 id="features">🎯 Features</h2>

<h3>1. Interactive Prediction Interface</h3>
<ul>
    <li>Input fields for four flower measurements:
        <ul>
            <li>Sepal Length (cm)</li>
            <li>Sepal Width (cm)</li>
            <li>Petal Length (cm)</li>
            <li>Petal Width (cm)</li>
        </ul>
    </li>
    <li>Toggle between KNN and Naive Bayes models</li>
    <li>Real-time species prediction (Setosa, Versicolor, Virginica)</li>
</ul>

<h3>2. Model Performance Dashboard</h3>
<ul>
    <li><strong>Training Results:</strong>
        <ul>
            <li>Accuracy score</li>
            <li>Classification report (Precision, Recall, F1-score, Support)</li>
            <li>Confusion matrix</li>
        </ul>
    </li>
    <li><strong>Testing Results:</strong>
        <ul>
            <li>Same comprehensive metrics for test data</li>
        </ul>
    </li>
    <li>Dynamic display based on selected model</li>
</ul>

<h3>3. Visual Design</h3>
<ul>
    <li>Modern glass-morphism UI with gradient background</li>
    <li>Responsive design (works on mobile and desktop)</li>
    <li>Smooth animations and hover effects</li>
    <li>Color-coded buttons and interactive elements</li>
</ul>

<hr>

<h2 id="live-demo">🌐 Live Demo</h2>

<p>Check out the live application:</p>
<ul>
    <li><strong>Render Deployment:</strong> <a href="https://iris-classifier-app.onrender.com">https://iris-classifier-app.onrender.com</a></li>
    <li><strong>GitHub Repository:</strong> <a href="https://github.com/hemalathapanchala/iris-classifier">https://github.com/hemalathapanchala/iris-classifier</a></li>
</ul>

<hr>

<h2 id="screenshots">📸 Screenshots</h2>
![image alt](https://github.com/hema1611/Knn_Navis_Iris_data_set/blob/9b6bdce904c2cf02667a000fa53b46edf47fba1b/Screenshot_14-2-2026_191017_knn-navis-iris-data-set.onrender.com.jpeg)
![image alt](https://github.com/hema1611/Knn_Navis_Iris_data_set/blob/9b6bdce904c2cf02667a000fa53b46edf47fba1b/Screenshot_14-2-2026_19938_knn-navis-iris-data-set.onrender.com.jpeg)
![Screenshot_14-2-2026_19938_knn-navis-iris-data-set onrender com](https://github.com/user-attachments/assets/62e4e76f-3f74-442b-b934-9beb3a41115a)


<p><em>(Add screenshots of your application here)</em></p>

<hr>

<h2 id="tech-stack">🛠️ Tech Stack</h2>

<h3>Frontend</h3>
<ul>
    <li>HTML5</li>
    <li>CSS3 (Custom animations, Glass-morphism)</li>
    <li>JavaScript (ES6)</li>
    <li>Bootstrap 5</li>
</ul>

<h3>Backend</h3>
<ul>
    <li>Python 3.8+</li>
    <li>Flask 3.1.2</li>
    <li>Jinja2 Templating</li>
    <li>Gunicorn (WSGI server)</li>
</ul>

<h3>Machine Learning</h3>
<ul>
    <li>scikit-learn 1.8.0</li>
    <li>NumPy 2.4.2</li>
    <li>Pandas 3.0.0</li>
    <li>Joblib 1.5.3</li>
    <li>KNN Classifier (k=3)</li>
    <li>Gaussian Naive Bayes</li>
</ul>

<h3>Deployment</h3>
<ul>
    <li>GitHub (Version Control)</li>
    <li>Render (Cloud Hosting)</li>
</ul>

<hr>

<h2 id="dataset">📊 Dataset</h2>

<p><strong>Source:</strong> Iris Dataset from Kaggle/UCI Machine Learning Repository</p>

<h3>Features:</h3>
<table border="1" cellpadding="5" cellspacing="0">
    <tr>
        <th>Feature</th>
        <th>Description</th>
        <th>Range</th>
    </tr>
    <tr>
        <td>Sepal Length</td>
        <td>Length of sepal in cm</td>
        <td>4.3 - 7.9</td>
    </tr>
    <tr>
        <td>Sepal Width</td>
        <td>Width of sepal in cm</td>
        <td>2.0 - 4.4</td>
    </tr>
    <tr>
        <td>Petal Length</td>
        <td>Length of petal in cm</td>
        <td>1.0 - 6.9</td>
    </tr>
    <tr>
        <td>Petal Width</td>
        <td>Width of petal in cm</td>
        <td>0.1 - 2.5</td>
    </tr>
</table>

<h3>Target Classes:</h3>
<table border="1" cellpadding="5" cellspacing="0">
    <tr>
        <th>Class</th>
        <th>Label</th>
        <th>Samples</th>
    </tr>
    <tr>
        <td>Iris Setosa</td>
        <td>0</td>
        <td>50</td>
    </tr>
    <tr>
        <td>Iris Versicolor</td>
        <td>1</td>
        <td>50</td>
    </tr>
    <tr>
        <td>Iris Virginica</td>
        <td>2</td>
        <td>50</td>
    </tr>
</table>

<hr>

<h2 id="model-performance">🧠 Model Performance</h2>

<h3>K-Nearest Neighbors (KNN)</h3>
<table border="1" cellpadding="5" cellspacing="0">
    <tr>
        <th>Metric</th>
        <th>Training</th>
        <th>Testing</th>
    </tr>
    <tr>
        <td><strong>Accuracy</strong></td>
        <td>95%</td>
        <td>100%</td>
    </tr>
    <tr>
        <td>Setosa F1-score</td>
        <td>1.00</td>
        <td>1.00</td>
    </tr>
    <tr>
        <td>Versicolor F1-score</td>
        <td>0.93</td>
        <td>1.00</td>
    </tr>
    <tr>
        <td>Virginica F1-score</td>
        <td>0.92</td>
        <td>1.00</td>
    </tr>
</table>

<h3>Naive Bayes (Gaussian)</h3>
<table border="1" cellpadding="5" cellspacing="0">
    <tr>
        <th>Metric</th>
        <th>Training</th>
        <th>Testing</th>
    </tr>
    <tr>
        <td><strong>Accuracy</strong></td>
        <td>95%</td>
        <td>100%</td>
    </tr>
    <tr>
        <td>Setosa F1-score</td>
        <td>1.00</td>
        <td>1.00</td>
    </tr>
    <tr>
        <td>Versicolor F1-score</td>
        <td>0.93</td>
        <td>1.00</td>
    </tr>
    <tr>
        <td>Virginica F1-score</td>
        <td>0.92</td>
        <td>1.00</td>
    </tr>
</table>

<h3>Confusion Matrices</h3>
<p>Both models show similar patterns:</p>
<ul>
    <li><strong>Training:</strong> 3 misclassifications between Versicolor and Virginica</li>
    <li><strong>Testing:</strong> Perfect classification (30/30 correct)</li>
</ul>

<hr>

<h2 id="installation">💻 Installation</h2>

<h3>Prerequisites</h3>
<ul>
    <li>Python 3.8+</li>
    <li>pip package manager</li>
    <li>Git (optional)</li>
</ul>

<h3>Setup Instructions</h3>

<pre>
<code>
# 1. Clone the repository
git clone https://github.com/hemalathapanchala/iris-classifier.git
cd iris-classifier

# 2. Create virtual environment (optional but recommended)
python -m venv venv

# On Windows:
venv\Scripts\activate

# On Mac/Linux:
source venv/bin/activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Run the application
python app.py

# 5. Open in browser
http://127.0.0.1:5000
</code>
</pre>

<hr>

<h2 id="usage">🎨 Usage Guide</h2>

<h3>Making Predictions</h3>
<ol>
    <li>Enter the four measurements in the input fields:
        <ul>
            <li>Sepal Length (cm)</li>
            <li>Sepal Width (cm)</li>
            <li>Petal Length (cm)</li>
            <li>Petal Width (cm)</li>
        </ul>
    </li>
    <li>Select model type:
        <ul>
            <li>Click <strong>"KNN"</strong> for K-Nearest Neighbors (default)</li>
            <li>Click <strong>"Naive Bayes"</strong> for Gaussian Naive Bayes</li>
        </ul>
    </li>
    <li>Click the <strong>"Predict"</strong> button</li>
    <li>View the predicted species below the button</li>
    <li>The right panel will automatically display model performance metrics</li>
</ol>

<h3>Viewing Results</h3>
<ul>
    <li><strong>Left Panel:</strong> Input form and prediction result</li>
    <li><strong>Right Panel:</strong> Training and testing metrics (appears after first prediction)</li>
</ul>

<hr>

<h2 id="project-structure">📁 Project Structure</h2>

<pre>
<code>
iris-classifier/
│
├── app.py                          # Main Flask application
├── requirements.txt                # Python dependencies
├── Procfile                        # Render deployment configuration
├── README.html                     # This file
│
├── templates/
│   └── index.html                  # Frontend template
│
├── Model Files/
│   ├── KNN.pkl                     # Trained KNN model
│   └── Navis.pkl                    # Trained Naive Bayes model
│
├── Metrics Files/
│   ├── train_knn.json              # KNN training metrics
│   ├── test_knn.json               # KNN testing metrics
│   ├── train_Navia.json             # NB training metrics
│   └── test_Navia.json              # NB testing metrics
│
└── Data/
    └── Iris (1).csv                 # Original dataset
</code>
</pre>

<hr>

<h2 id="deployment">🚀 Deployment on Render</h2>

<h3>Step-by-Step Deployment Guide</h3>

<h4>1. Prepare Files</h4>
<p>Ensure you have these files in your repository:</p>
<ul>
    <li><code>requirements.txt</code> - Dependencies list</li>
    <li><code>Procfile</code> - Contains: <code>web: gunicorn app:app</code></li>
    <li><code>app.py</code> - Main application</li>
    <li><code>templates/index.html</code> - Frontend template</li>
    <li>All model and metrics files (.pkl, .json)</li>
</ul>

<h4>2. Upload to GitHub</h4>
<pre>
<code>
git init
git add .
git commit -m "Initial commit: Iris Classification App"
git branch -M main
git remote add origin https://github.com/hemalathapanchala/iris-classifier.git
git push -u origin main
</code>
</pre>

<h4>3. Deploy on Render</h4>
<ol>
    <li>Sign up/Login at <a href="https://render.com">render.com</a></li>
    <li>Click <strong>"New +"</strong> → <strong>"Web Service"</strong></li>
    <li>Connect your GitHub repository</li>
    <li>Configure:
        <ul>
            <li><strong>Name:</strong> iris-classifier-app</li>
            <li><strong>Environment:</strong> Python 3</li>
            <li><strong>Build Command:</strong> <code>pip install -r requirements.txt</code></li>
            <li><strong>Start Command:</strong> <code>gunicorn app:app</code></li>
        </ul>
    </li>
    <li>Click <strong>"Create Web Service"</strong></li>
</ol>

<h4>4. Access Your App</h4>
<p>Render will provide a URL like: <code>https://iris-classifier-app.onrender.com</code></p>

<hr>

<h2 id="troubleshooting">⚠️ Troubleshooting</h2>

<h3>Common Issues & Solutions</h3>

<table border="1" cellpadding="5" cellspacing="0">
    <tr>
        <th>Issue</th>
        <th>Solution</th>
    </tr>
    <tr>
        <td>Model not loading</td>
        <td>Check file paths and pickle versions. Ensure .pkl files are in the root directory.</td>
    </tr>
    <tr>
        <td>JSON decode error</td>
        <td>Verify JSON files are properly formatted. Check for missing commas or brackets.</td>
    </tr>
    <tr>
        <td>Prediction error</td>
        <td>Ensure input values are numbers (decimals allowed). Check Flask route for exceptions.</td>
    </tr>
    <tr>
        <td>Render deployment fails</td>
        <td>Verify Procfile contains <code>web: gunicorn app:app</code>. Check build logs for errors.</td>
    </tr>
    <tr>
        <td>No right panel showing</td>
        <td>Make a prediction first. The panel only appears after prediction.</td>
    </tr>
    <tr>
        <td>Module not found</td>
        <td>Run <code>pip install -r requirements.txt</code> to install all dependencies.</td>
    </tr>
</table>

<h3>Render-Specific Tips</h3>
<ul>
    <li>Use <code>gunicorn app:app</code> in Procfile (not <code>python app.py</code>)</li>
    <li>Ensure all file paths are relative (not absolute)</li>
    <li>Check build logs in Render dashboard for errors</li>
    <li>Free tier spins down after inactivity - first request may take 30-60 seconds</li>
</ul>

<hr>

<h2 id="future-enhancements">🔮 Future Enhancements</h2>

<ol>
    <li><strong>Add more algorithms</strong> (Decision Tree, SVM, Random Forest)</li>
    <li><strong>Data visualization</strong> with plots and charts using Matplotlib/Plotly</li>
    <li><strong>Batch prediction</strong> from CSV file upload</li>
    <li><strong>Model retraining</strong> capability with user data</li>
    <li><strong>User accounts</strong> to save prediction history</li>
    <li><strong>API endpoints</strong> for programmatic access</li>
    <li><strong>Feature importance</strong> visualization</li>
    <li><strong>Cross-validation</strong> results display</li>
    <li><strong>Download reports</strong> as PDF/CSV</li>
    <li><strong>Multi-language support</strong></li>
</ol>

<hr>

<h2 id="contact">📞 Contact & Support</h2>

<p>For issues, questions, or collaboration opportunities:</p>

<ul>
    <li><strong>Email:</strong> <a href="mailto:hemalathapanchala31@gmail.com">hemalathapanchala31@gmail.com</a></li>
    <li><strong>LinkedIn:</strong> <a href="https://www.linkedin.com/in/hemalatha-panchala-">Hemalatha Panchala</a></li>
    <li><strong>GitHub:</strong> <a href="https://github.com/hemalathapanchala">@hemalathapanchala</a></li>
    <li><strong>Project Repository:</strong> <a href="https://github.com/hemalathapanchala/iris-classifier">github.com/hemalathapanchala/iris-classifier</a></li>
    <li><strong>Live Demo:</strong> <a href="https://iris-classifier-app.onrender.com">iris-classifier-app.onrender.com</a></li>
</ul>

<hr>

<h2 id="license">📄 License</h2>

<p>This project is open-source and available for educational and commercial use.</p>

<hr>

<h2>🙏 Acknowledgements</h2>

<ul>
    <li>Iris dataset from UCI Machine Learning Repository</li>
    <li>Scikit-learn for ML algorithms</li>
    <li>Flask framework documentation</li>
    <li>Bootstrap 5 for UI components</li>
    <li>Render for free hosting</li>
</ul>

<hr>

<h1 align="center">🌸 Happy Classifying! 🌸</h1>

<p align="center">
    <i>Created with ❤️ by Hemalatha Panchala</i>
</p>

<p align="center">
    <b>If you find this project useful, please give it a ⭐ on GitHub!</b>
</p>

</body>
</html>
