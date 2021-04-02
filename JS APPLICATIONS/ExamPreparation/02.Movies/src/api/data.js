import * as api from './api.js';

import {host} from './api.js';


async function login(email, password) {
    return await api.apiLogin(host + '/users/login',email,password);
}

async function register(email, password) {
    return await api.apiRegister(host + '/users/register',email,password);
}

async function logout() {
    return await api.apiLogout(host + '/users/logout');
}

async function getItems() {
    return await api.get(host + '/data/movies');
}

async function getItemId(id) {
    return await api.get(host + '/data/movies/' + id);
}

async function getUserItems() {
    let userId = sessionStorage.getItem('userId');
    return await api.get(host + `/data/catalog?where=_ownerId%3D%22${userId}%22`);
}

async function createRecord(data) {
    return await api.post(host + '/data/movies', data);
}

async function editRecord(id, data) {
    return await api.put(host + '/data/movies/' + id, data);
}

async function deleteRecord(id) {
    // TODO Check if id exists!!!
    return await api.del(host + '/data/movies/' + id);
}

export async function getLikes(movieId) {
    return await api.get(host + `/data/likes?where=movieId%3D%22${movieId}%22&distinct=_ownerId&count`);
}
export async function getUserLike(movieId) {
    let userId = sessionStorage.getItem('userId');
    return await api.get(host + `/data/likes?where=movieId%3D%22${movieId}%22%20and%20_ownerId%3D%22${userId}%22`);
}
export async function addLike(data) {
    return await api.post(host + `/data/likes`,data);
}
export async function unLike(id) {
    return await api.del(host + `/data/likes/` + id);
}


export {
    getItems,
    getItemId,
    getUserItems,
    createRecord,
    editRecord,
    deleteRecord,
    login,
    register,
    logout,
};

// //for testing purposes
// window.login=login
// window.register=register
// window.logout=logout
// window.getItems=getItems
// window.getItemId=getItemId
// window.getUserItems=getUserItems
// window.createRecord=createRecord
// window.editRecord=editRecord
// window.deleteRecord=deleteRecord
// window.getLikes=getLikes
// window.getUserLike=getUserLike
// window.adLike=adLike
// window.unLike=unLike

