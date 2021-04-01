export const host = 'http://localhost:3030';

async function request(url, options) {
    try {
        let response = await fetch(url, options);
        if (response.ok == false) {
            let error = await response.json();

            throw new Error(error.message);
        }
        try {
            let data = await response.json();
            return data;
        } catch (error) {
            return response;
        }

    } catch (error) {
        alert(error.message);
        throw error;
    }
}

function getOptions(method = 'get', body) {
    const options = {
        method: method,
        headers: {}
    };
    const token = sessionStorage.getItem('authToken');
    if (token != null) {
        options.headers['X-Authorization'] = token;
    }
    if (body) {
        options.headers['Content-Type'] = 'application/json';
        options.body = JSON.stringify(body);
    }
    return options;
}

async function get(url) {
    return await request(url, getOptions());
}

async function post(url, data) {
    return await request(url, getOptions('post', data));
}

async function put(url, data) {
    return await request(url, getOptions('put', data));
}

async function del(url) {
    return await request(url, getOptions('delete'));
}

async function apiLogin(url, username, password) {
    let result = await post(url, {username: username, password});
    sessionStorage.setItem('username', result.username);
    sessionStorage.setItem('authToken', result.accessToken);
    sessionStorage.setItem('userId', result._id);
}

async function apiRegister(url,username, password) {
    let result = await post(url, {username, password});
    sessionStorage.setItem('username', result.username);
    sessionStorage.setItem('authToken', result.accessToken);
    sessionStorage.setItem('userId', result._id);
}

function apiLogout(url) {
    //TODO - correct when account token doesn't match
    get(url);
    sessionStorage.clear()
}


export {
    get,
    post,
    put,
    del,
    apiLogin,
    apiRegister,
    apiLogout,
};


