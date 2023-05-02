pytest -s -v -m "regression" --html=reports\html_reports02.html .\testCases --browser chrome
REM pytest -s -v -m "regression or sanity" --html=reports\html_reports02.html .\testCases --browser chrome 
REM pytest -s -v --html=reports\html_reports02.html .\testCases --browser chrome 
REM pytest -s -v -m "sanity" --html=reports\html_reports02.html .\testCases --browser chrome 

REM pytest -s -v -m "regression" --html=reports\html_reports02.html .\testCases --browser chrome
REM pytest -s -v -m "regression or sanity" --html=reports\html_reports02.html .\testCases --browser chrome 
REM pytest -s -v --html=reports\html_reports02.html .\testCases --browser chrome 
pytest -s -v -m "sanity" --html=reports\html_reports02.html .\testCases --browser edge 