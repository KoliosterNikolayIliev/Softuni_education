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
    return await api.get(host + '/data/wiki?sortBy=_createdOn%20desc');
}
async function getHomeItems() {
    return await api.get(host + '/data/wiki?sortBy=_createdOn%20desc&distinct=category');
}

async function getItemId(id) {
    return await api.get(host + '/data/wiki/' + id);
}

async function getUserItems() {
    let userId = sessionStorage.getItem('userId');
    return await api.get(host + `/data/catalog?where=_ownerId%3D%22${userId}%22`);
}

async function createRecord(data) {
    return await api.post(host + '/data/wiki', data);
}

async function editRecord(id, data) {
    return await api.put(host + '/data/wiki/' + id, data);
}

async function deleteRecord(id) {
    return await api.del(host + '/data/wiki/' + id);
}
async function getsearchItems(query) {
    return await api.get(host + `/data/wiki?where=title%20LIKE%20%22${query}%22`);
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
    getHomeItems,
    getsearchItems,
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

