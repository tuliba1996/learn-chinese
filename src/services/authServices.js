import api from '@/services/api'




const login = (payload) =>{
    return api.post(`token/`, payload)
        .then(handleResponse)
        .then(data => {
            // login successful if there's a jwt token in the response
            if (data.token) {
                // store user details and jwt token in local storage to keep user logged in between page refreshes
                localStorage.setItem('user', JSON.stringify(data));
            }
            return data;
        })
}


function logout() {
    // remove user from local storage to log user out
    localStorage.removeItem('user');
}


const  handleResponse = (response) => {
    if (response.statusText !== 'OK') {
        if (response.status === 401) {
            // auto logout if 401 response returned from api
            logout();
            location.reload(true);
        }
        const error = (response.data && response.data.message) || response.statusText;
        return Promise.reject(error);
    }
    return response.data
}


export const authServices = {
    login,
    logout
}