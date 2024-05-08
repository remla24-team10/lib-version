# lib-version
This is a package that returns the version of itself. 

### Building the package locally
1. ```poetry install```
2. ```poetry shell```
3. ```poetry build```
<!-- 3. ```python3 -m build```
To upload to PyPi you need to have access to the API key, which is stored in the team channel -->
1. ```python3 -m twine upload --repository pypi dist/*``` 

### Updating the package via workflow
After pushing an update you can tag it with the following command to trigger the workflow.
1. ```git tag v0.0.n```
2. ```git push origin --tags ```

### Importing the package
1. Install with: ```pip install --index-url https://pypi.org/project/ --no-deps lib-version-remla```