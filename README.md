## How to setup the project

### 1. Clone the repository

```shell
git clone 
```
### 2. Create virtual environment

```shell
python3 -m venv venv
```

### 3. Install requirements.txt

```shell
pip install -r requirements.txt
```

### 4. Copy env-sample.py to env.py 

```shell
cp src/settings/env-sample.py src/settings/env.py
```

### 5. Configure Database 

```markdown
1. Check the env.py
2. Replace the DATABASES config with your config
```


### 6. Configure Pre-commit

```shell
# ref https://pre-commit.com/

pre-commit install 

# optional 
pre-commit run --all-files
```

