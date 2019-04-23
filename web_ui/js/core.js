let ask_question = function() {
  question = document.querySelector('#question').value;
  ask(question, '').then(data => fill_answers(data['result']));
}

let ask = function(question, config) {
  return postData('//localhost:7001/api/v1/run', {
      question: question,
      config: config
    })
    .then(response => response.json());
}

let pipelines = function() {
  return fetch('//localhost:7001/api/v1/pipelines')
    .then(response => response.json());
}

let postData = function(url = '', data = {}) {
    return fetch(url, {
        method: 'POST',
        mode: 'cors',
        cache: 'no-cache',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(data),
    });
}

let fill_algorithm = function(values) {
  let algorithm = document.querySelector('#algorithm');
  values.forEach(function(text, i) {
    var opt = document.createElement('option');
    opt.value = i
    opt.text = text
    algorithm.add(opt)
  })
}

let fill_answers = function(values) {
  let answers = document.querySelector('#answers');
  answers.innerHTML = '';
  values.forEach(function(text) {
    var text = text.split(',')
    text[1] = text[1].replace('><', ',')
    text[1] = text[1].replace('<', '')
    text[1] = text[1].replace('>', '')
    var li = document.createElement('li');
    li.classList.add('p-list__item')
    li.classList.add('is-ticked')
    li.innerHTML = `${parseFloat(text[0]).toFixed(4)} ${text[1]}`
    answers.append(li)
  })
}

// load settings
pipelines().then(data => fill_algorithm(data['pipelines']));
