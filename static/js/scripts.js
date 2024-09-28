class AjaxManager {
    constructor(loaderSelector, responseMessageSelector) {
        this.loader = $(loaderSelector);
        this.responseMessage = $(responseMessageSelector);
    }

    showLoader() {
        this.loader.show();
    }

    hideLoader() {
        this.loader.hide();
    }

    resetForm(formSelector) {
        $(formSelector)[0].reset();
    }

    showMessage(type, message) {
        const alertType = type === 'success' ? 'alert-success' : 'alert-danger';
        this.responseMessage.html(`<div class="alert ${alertType}">${message}</div>`);
    }

    getFormData(formSelector) {
        console.log("formSelector", formSelector)
        const formDataArray = $(formSelector).serializeArray();
        const formData = {};
        formDataArray.forEach(item => {
            if (item.name === 'parent' && item.value === '') {
                formData[item.name] = null;  // Set to null if empty
            } else {
                formData[item.name] = item.value;
            }
        });
        return formData;
    }

    ajaxRequest(method, url, data, successCallback) {
        this.showLoader();
        console.log(">>>", method, url, data)
        $.ajax({
            type: method,
            url: url,
            contentType: 'application/json',
            data: JSON.stringify(data),
            success: (response) => {
                successCallback(response);
            },
            error: (xhr, status, error) => {
                this.showMessage('error', `Error: ${xhr.responseText}`);
            },
            complete: () => {
                this.hideLoader();
            }
        });
    }
}
