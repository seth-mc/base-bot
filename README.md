# Base Bot

Welcome to the Base Bot - which will be the launch pad for our project! Check out the Lucid Chart here:

    [IN PROGRESS]

Here's how it works through a diagram I made:

```
![Diagram](https://assets.codepen.io/6932556/cryptobot-explained.gif)
```

### To add the repository to your own computer:

#### The manual approach:
1. Click Code > Download ZIP.
2. Open the ZIP file and put it somewhere nice. 
3. Tinker with the code. If you want to make changes and push them back, you will need to folow the cool coding approach. 

#### The cool coding approach:
1. Ensure you have Git installed
```
git --version
```
2. Create a new file for your GitHub documents.
3. Copy the filepath by going Edit > click "Alt" and select 'Copy "GitHub" as Filename'. 
4. open Terminal. Enter the following:
```
cd [paste FILEPATH to base-bot]
```
5. clone the repo on in to your GitHub file:
```
git clone https://github.com/seth-mc/base-bot.git
```


### After making changes to the repository:
1. open Terminal. Enter the following:
```
cd [FILEPATH to GitHub]
```

2. Then, either add the URL (Or set-URL if you get a "fatal: remote origin already exists" error)

```
git remote add origin https://github.com/seth-mc/base-bot.git

git remote set-url origin https://github.com/seth-mc/base-bot.git

```

3. Update the files with your new code:


    To add all the changes you've made:
        ```
        git add .
        ```
    To add single folder:
        ```
        git add directory path
        ```
   To add multiple folders:
        ```
        git add folder1 folder2 folder3 folder4
        ```

```
git add .
git commit -m "enter description here"
git push origin main
```

### If you want to pull the latest changes to your existing folder:
1. open Terminal. Enter the following:
```
cd [paste FILEPATH to base-bot]
```
2. to a pull from the main branch:
```
git pull origin main
```


