// FIRST TEST APPROACH, NO TIME TO MAKE A REAL TEST
// THE BODY IN THE FETCHPARAMETERS MUST BE JSON.STRINGIFY TO WORK
// TO AVOID CORS SHIT, COPY AND PASTE CODE IN http://localhost:8080/post in a console in the web browser
// NEED TO IMPROVE THIS, BUT THIS IS THE MOST QUICK APPROACH RIGHT NOW

url = 'http://localhost:8000/post'

const fetchParameters = {
    method:'POST',
    body: JSON.stringify({name:'tere'})
}

async function postUser(urlToPost){
    let data = await fetch(urlToPost, fetchParameters);
    console.log(data)
   
}

postUser(url)