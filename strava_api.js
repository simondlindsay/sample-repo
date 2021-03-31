
const auth_link = "https://www.strava.com/oauth/token" 

function getActivities(res) {
    const activities_link = `https://www.strava.com/api/v3/athlete/activities?access_token=${res.access_token}`
    fetch(activities_link)
        .then((res) => console.log(res.json()))
}


function reAuthorize(){
    fetch(auth_link,{
        method: 'post',
        headers: {
            'Accept': 'application/json, text/plain, */*',
            'Content-Type': 'application/json'
        },

        body: JSON.stringify({

            client_id: "63295",
            client_secret: "1f85787294f3846b9b5b16e54913aeff4919fade", 
            refresh_token: "ecbb8e1b89a88c54a7498d6da63fbfabab854474",
            grant_type: "refresh_token"
        })
    }).then(res => res.json())
        .then(res => getActivities(res))
}

reAuthorize()