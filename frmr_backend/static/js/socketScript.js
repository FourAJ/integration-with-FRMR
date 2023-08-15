$(document).ready(function () {
    let requests = document.querySelectorAll('[data-request]');
    let socket = io.connect(location.protocol + '//' + document.domain + ':' + location.port + namespace);

    socket.on('socket', function () {
        requests.forEach((request) => {
            let drop = request.querySelector('[data-drop]')
            let menu = request.querySelector('[data-menu]')
            let img = drop.querySelector('img')
            let execute = menu.querySelector('[data-execute]')
            let loader = menu.querySelector('[data-loader]')
            let responseBlocks = menu.querySelectorAll('.r_response')

            let mr_btn = menu.querySelector('#mr')
            if (mr_btn) {
                let mr_label = mr_btn.querySelector('label')
                let mr_checkbox = mr_btn.querySelector('input')

                mr_btn.addEventListener('click', () => {
                    if (mr_checkbox.checked) {
                        mr_checkbox.checked = false;
                        mr_checkbox.value = false;
                        mr_label.textContent = 'False';
                        mr_label.style.color = "#8F8F8F";
                    } else {
                        mr_checkbox.checked = true;
                        mr_checkbox.value = true
                        mr_label.textContent = 'True';
                        mr_label.style.color = "#ffffff";
                    }
                });
            }

            let inputDate = request.querySelector('[data-date]')
            $(inputDate).inputmask({
                mask: '9999-99-99T99:99:99.9999999Z',
                placeholder: '____-__-__T__:__:__._______Z',
                clearIncomplete: true
            });


            drop.addEventListener('click', () => {
                if (img.classList.contains('rotated')) {
                    img.classList.remove('rotated');
                    img.style.transform = 'rotate(0deg)';
                } else {
                    img.classList.add('rotated');
                    img.style.transform = 'rotate(180deg)';
                }
                if (menu.classList.contains('hidden')) {
                    menu.classList.remove('hidden');
                    menu.style.visibility = '';
                    menu.style.position = '';
                } else {
                    menu.classList.add('hidden');
                    menu.style.visibility = 'hidden';
                    menu.style.position = 'absolute';
                }
                if (drop.classList.contains('open')) {
                    drop.classList.remove('open');
                    drop.style.borderRadius = "15px"
                } else {
                    drop.classList.add('open');
                    drop.style.borderRadius = "15px 15px 0 0"
                }
            });

            execute.addEventListener('click', () => {
                let inputParams = menu.querySelectorAll('[data-input]')
                let payload = {'endpoint': drop.querySelector('#endpoint').innerHTML}

                inputParams.forEach((inputParam) => {
                    let param = inputParam.querySelector('input')
                    if (param) {
                        payload[`${param.id}`] = validation(param.value)
                    }
                })

                loader.style.visibility = '';
                responseBlocks.forEach((response) => {
                    response.style.filter = 'blur(2px)';
                })
                socket.emit("payload", payload);


                socket.on('payload', function (res) {
                    if (drop.querySelector('#endpoint').innerHTML === res[2]) {
                        let jsonPlaces = menu.querySelectorAll('[data-json]')
                        jsonPlaces.forEach((place) => {
                            if (place.id === 'json200') {
                                place.innerHTML = 'Ok'
                            }
                            if (place.id === 'json400') {
                                place.innerHTML = 'Bad request'
                            }
                            if (place.id === 'json403') {
                                place.innerHTML = 'Forbidden'
                            }
                            if (place.id === 'json404') {
                                place.innerHTML = 'Not Found'
                            }
                            if (place.id === 'json500') {
                                place.innerHTML = 'Internal Server Error'
                            }
                        })

                        loader.style.visibility = 'hidden';

                        responseBlocks.forEach((response) => {
                            response.style.filter = '';
                        })


                        let jsonPlace = menu.querySelector(`#json${res[3]}`)
                        jsonPlace.innerHTML = JSON.stringify(res[0], null, 2)

                        let urlPlace = menu.querySelector('#url')
                        let urlBlock = menu.querySelector('#urlBlock')
                        urlBlock.style.visibility = '';
                        urlBlock.style.position = '';
                        urlPlace.innerHTML = res[1]
                    }
                })
            });
        });
    });

    function validation(arg) {
        if (arg !== '') {
            return arg;
        } else {
            return null;
        }
    }
});