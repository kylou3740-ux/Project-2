# Lab 20 --- Partner Cold-Run Note

## 1. Cold-run setup

-   **Starting point:** Tester received only the repository link and
    followed the instructions in `README.md`.
-   **Project command:** `streamlit run app.py`

## 2. Partner observations

**Partner comment :**

> "The README was pretty straightforward, nothing too confusing. On the
> first run, the app didn't launch properly because one of the required
> packages wasn't installed into my enviornment, but after I installed it,
> it opened fine. 

**First failure:**

The application did not start on the first attempt. The
terminal displayed a `ModuleNotFoundError` message.

**Elapsed time:**

Approximately 8 minutes from opening the repository, including time
spent resolving the error.

**Result location:**

The Streamlit application opened in the browser. The tester
located the results on the main page.

## 3. Fix and retest

**Fix:**

Make sure the README is more clear about what dependencies a new
user needs to install before they can launch the application. There 
also wasn't a requirements file in the repository, so making sure to
include one. 


**Retest result:**

After installing the dependencies, the tester reran the application and
was able to open it and locate the output.

