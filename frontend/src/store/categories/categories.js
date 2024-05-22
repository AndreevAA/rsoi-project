import axios from "axios";/*
import router from "../../router/index"*/
import defaultModule from "@/store/defaultModule";

const     state = {
    categories: '',

}

const actions = {
    //Получить все категории
    get_categories: (({commit}, namespaceId) => {
        let config = {
            method: 'get',
            url: 'http://158.160.164.167/api/category-service/categories/?namespace_id=' + namespaceId.namespaceId,
            headers: {
                'Authorization': 'Bearer ' + defaultModule.state.token
            }
        };
        axios(config)
            .then(function (response) {
                commit('set_categories', response.data)
            })
            .catch(function (error) {
                console.log(error);
                console.log(error.response)
            });
    }),
}
const mutations = {
    set_categories: (state, categories) => {
        state.categories = categories
    },
    //Создать категорию
    post_category: (state, data) => {
        let config = {
            method: 'post',
            url: 'http://158.160.164.167/api/category-service/categories/',
            headers: {
                'Authorization': 'Bearer ' + defaultModule.state.token
            },
            data: {
                'name': data.categoryName,
                'namespace_id': data.namespaceId
            }
        };
        axios(config)
            .then(function () {
            })
            .catch(function (error) {
                console.log(error);
                console.log(error.response)
            });
    },

    //Удалтиь категорию
    delete_category: (state, categoryId) => {
        let config = {
            method: 'delete',
            url: 'http://158.160.164.167/api/category-service/categories/' + categoryId.categoryId,
            headers: {
                'Authorization': 'Bearer ' + defaultModule.state.token
            }
        };
        axios(config)
            .then(function () {
            })
            .catch(function (error) {
                console.log(error);
                console.log(error.response)
            });
    }
}
const  getters = {
    categories(state) {
        return state.categories
    },
}


export default {
    state,
    actions,
    mutations,
    getters
}