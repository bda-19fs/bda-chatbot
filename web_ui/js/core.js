let ask_question = function() {
  console.time('ask_question');
  question = document.querySelector('#question').value;
  config = load_config();
  ask(question, config).then(result => {
    fill_tfidf_answers(result['tfidf']);
    fill_skipgram_answers(result['skip_gram']);
  });
  console.timeEnd('ask_question');
}

let load_config = function() {
  return {
    'dataset': document.querySelector('#dataset').value,
    'algorithm': document.querySelector('#algorithm').value,
    'domain_limit': document.querySelector('#domain_limit').value
  };
}

let ask = function(question, config) {
  return post_data('//localhost:7001/api/v1/run', {
      question: question,
      config: config
    })
    .then(response => response.json());
}

let pipelines = function() {
  return fetch('//localhost:7001/api/v1/pipelines')
    .then(response => response.json());
}

let post_data = function(url = '', data = {}) {
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

let fill_settings = function(id, values) {
  let select = document.querySelector(`#${id}`);
  values.forEach(function(text, i) {
    var opt = document.createElement('option');
    opt.value = i
    opt.text = text
    select.add(opt)
  })
}

let fill_tfidf_answers = function(values) {
  let tfidf_answers = document.querySelector('#tfidf_answers');
  tfidf_answers.innerHTML = '';
  values[0].forEach(function(text) {
    var text = text.split(',')
    text[1] = text[1].replace('><', ',')
    text[1] = text[1].replace('<', '')
    text[1] = text[1].replace('>', '')
    var li = document.createElement('li');
    li.classList.add('p-list__item')
    li.classList.add('is-ticked')
    li.innerHTML = `${parseFloat(text[0]).toFixed(4)} ${text[1]}`
    tfidf_answers.append(li)
  })
}

let fill_skipgram_answers = function(values) {
  let skipgram_answers = document.querySelector('#skipgram_answers');
  skipgram_answers.innerHTML = '';
  values.forEach(function(text) {
    var text = text.split(',')
    text[1] = text[1].replace('><', ',')
    text[1] = text[1].replace('<', '')
    text[1] = text[1].replace('>', '')
    var li = document.createElement('li');
    li.classList.add('p-list__item')
    li.classList.add('is-ticked')
    li.innerHTML = `${parseFloat(text[0]).toFixed(4)} ${text[1]}`
    skipgram_answers.append(li)
  })
}

// load settings
pipelines().then(data => {
  const {dataset, algorithm, domain_limit} = data;
  fill_settings('dataset', dataset);
  fill_settings('algorithm', algorithm);
  fill_settings('domain_limit', domain_limit);
});

// empty questions
document.querySelector('#question').value = ''
