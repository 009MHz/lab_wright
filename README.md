# Pre requisites
Before getting started, make sure your local IDE & config follow the repository criteria.
Run this command to install required dependencies
```bash
pip install -r requirements.txt
```

# Directory Structure:
- `resources`: store the required assets from each test execution
  - `/PERSONA`: store any assets, locators / credentials for each account type
  - `/LANDING`: store any assets/locators related to the main landing page testfile (https://www.karirlab.co/job)
  - `/JOB`: store any assets/locators related to the main landing page testfile (https://www.karirlab.co/job)
  - `/RESUME_BUILDER`: store any assets/locators related to the main landing page testfile (https://www.karirlab.co/resume-builder)


- `tests`: store the created test scripts that will be collected into each feature/page directory:
  - `tests/LANDING`: store any test cases related to the main landing page
  - `tests/JOB`: store any test cases related to the JOB page
  - `tests/RESUME_BUILDER`: store any test cases related to the resume builder feature

# Git Pattern
### Branch Naming: 
- `master`: main source branch
  - `beta`: in development branch, unpublished to *Production/master* <br>
  => `beta__{page/feature_name}` => `beta__resume_builder`

### Commit pattern:
-  `{PARENT_JOB}-{subTaskName}-{subTaskName}: Action Name` <br>
  => `JOB-listJob-filter: Define element locator`

## Guidance Template
This is the simplest template to start from.

- Get started from a simple task template in `tasks.robot`.
  - Uses [Robot Framework](https://robocorp.com/docs/languages-and-frameworks/robot-framework/basics) syntax.
- You can configure your robot `robot.yaml`.
- You can configure dependencies in `conda.yaml`.

## Learning materials

- [Robocorp Developer Training Courses](https://robocorp.com/docs/courses)
- [Documentation links on Robot Framework](https://robocorp.com/docs/languages-and-frameworks/robot-framework)
- [Example bots in Robocorp Portal](https://robocorp.com/portal)
