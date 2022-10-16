## Venv setup

I use venv for python and this will be ignored from github. Therefore go to your /winterweek/api folder and do this for Linux:

```
$ python3 -m venv venv
$ source venv/bin/activate
(venv) $ _
```
Or Windows instead:

```
$ python -m venv venv
$ venv\Scripts\activate
(venv) $ _
```

and install the python dependencies in the venv (make sure you activated the venv as mentioned above and that you are in the /winterweek/api folder)

```pip3 install -r requirements.txt```

## Setup credentials for mailbot

place a pw.txt file in /winterweek/api with the sender email pw.

# Getting the app to run in dev mode

This project was bootstrapped with [Create React App](https://github.com/facebook/create-react-app).

## Run frontend 

Go to the /winterweek folder in the project directory

### `yarn start`

Runs the app in the development mode.\
Open [http://localhost:3000](http://localhost:3000) to view it in your browser.

The page will reload when you make changes.\
You may also see any lint errors in the console.

## Build the frontend for deployment

In case you want to update the deployed version. Go to the /winterweek folder in the project directory

### `yarn build`

this will give you a /build folder that you can copy into a deployed environment to update the frontend.

## Run backend 

Open a new terminal. Go to the /winterweek folder in the project directory

### `yarn start-api`

Runs the backend as a flask application


## Deployment of the whole app

Check out this step-by-step guide from Miguel Grinberg: https://blog.miguelgrinberg.com/post/how-to-deploy-a-react--flask-project
