# plagiarism-checker
SPA project for detecting plagiarism in documents, with a focus on identifying content generated by large language models (LLMs), aimed at supporting French high school teachers.

You can visit our project at here : http://146.59.237.23/

## For dev purposes

### Prerequisites
- Node.js version 18.x (to run the frontend)
- Vue.js (used for the frontend)
- Python (for data processing)
  
### Installation

```sh
git clone git@github.com:valentinefleith/plagiarism-checker.git && cd plagiarism-checker
```

Download python dependencies:
```
make setup
```


### Start backend server

You can pull the model using `git lfs`. If it's not available for you, the model is downloadable [here](https://drive.google.com/drive/folders/1Y0Nees4Q0ghGcsctCkXw9fI_qvv0QOEn?usp=sharing).

Then to start the server run:
```
make run
```

## Project setup
Navigate to the frontend directory
```
cd frontend
```

### Install dependencies:
```
npm install
```

### Start the development server with hot-reload
```
npm run serve
```
