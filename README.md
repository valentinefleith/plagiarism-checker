# plagiarism-checker
Plagiarism detection tool for french high school teachers

### Prerequisites
- Node.js version 18.x 
### Installation

```sh
git clone git@github.com:valentinefleith/plagiarism-checker.git && cd plagiarism-checker
```

### Download data

```sh
make corpus
```
If not working:
```sh
make
.venv/bin/python src/corpus/download_corpus.py
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
