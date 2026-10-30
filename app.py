from flask import Flask, render_template, request
from phishing_checker import analyze_url

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    submitted_url = ""
    warnings = None
    error = None

    if request.method == "POST":
        submitted_url = request.form.get("url", "").strip()
        if not submitted_url:
            error = "Please enter a URL to check."
        else:
            warnings = analyze_url(submitted_url)
            if warnings and warnings[0] in (
                "Please enter a URL.",
                "The URL does not contain a recognizable hostname.",
            ):
                error = warnings[0]
                warnings = None

    return render_template(
        "index.html",
        submitted_url=submitted_url,
        warnings=warnings,
        error=error,
    )

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
