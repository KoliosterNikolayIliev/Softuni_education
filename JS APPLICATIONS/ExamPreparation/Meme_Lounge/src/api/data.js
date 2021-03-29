import * as api from './api.js';

import {host} from './api.js';


async function login(email, password) {
    return await api.apiLogin(host + '/users/login',email,password);
}

async function register(email, password, username, gender) {
    return await api.apiRegister(host + '/users/register',email,password,username,gender);
}

async function logout() {
    return await api.apiLogout(host + '/users/logout');
}

async function getItems() {
    return await api.get(host + '/data/memes?sortBy=_createdOn%20desc');
}

async function getItemId(id) {
    return await api.get(host + '/data/memes/' + id);
}

async function getUserItems() {
    let userId = sessionStorage.getItem('userId');
    return await api.get(host + `/data/memes?where=_ownerId%3D%22${userId}%22&sortBy=_createdOn%20desc`);
}

async function createRecord(data) {
    return await api.post(host + '/data/memes', data);
}

async function editRecord(id, data) {
    return await api.put(host + '/data/memes/' + id, data);
}

async function deleteRecord(id) {
    // TODO Check if id exists!!!
    return await api.del(host + '/data/memes/' + id);
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

