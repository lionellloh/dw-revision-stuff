import requests
response = requests.get('https://fakerinos-staging.herokuapp.com/api/articles/', headers={'Authorization': 'Token f32c6bc9e84da7bf8c15f2665d6e39ea6b988baa'})

print(response.body)