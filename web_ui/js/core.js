let ask_question = function() {
  console.time('ask_question');
  question = document.querySelector('#question').value;
  config = load_config();
  ask(question, config).then(result => {
    console.table(result['tfidf_questions']);
    fill_answers('tfidf_answers', result['tfidf_tags'], result['tfidf_answers'], result['tfidf_questions']);
    fill_answers('skipgram_answers', result['w2v_tags'], result['w2v_answers'], result['w2v_questions']);
    console.timeEnd('ask_question');
  });
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
    opt.value = i;
    opt.text = text;
    select.add(opt);
  })
}

let fill_answers = function(id, tags, answer, question) {
  console.log(question[0]);
  let answers = document.querySelector(`#${id}`);
  answers.innerHTML = '';
  tags.forEach(function(text, i) {
    var text = text.split(',')
    var li = document.createElement('li');
    li.classList.add('p-list__item');
    li.classList.add('is-ticked');
    li.classList.add('p-accordion__group');
    var button = document.createElement('button');
    button.innerHTML = `${parseFloat(text[0]).toFixed(4)} ${text[1]}`;
    button.classList.add('p-accordion__tab');
    button.setAttribute('aria-expanded', true);
    button.onclick = function() { toggle_answer(this); };
    var question_title = document.createElement('h5');
    question_title.innerHTML = 'Question';
    var question_p = document.createElement('p');
    question_p.innerHTML = question[i].split(',')[1];
    var answer_title = document.createElement('h5');
    answer_title.innerHTML = 'Answer';
    var answer_p = document.createElement('p');
    answer_p.innerHTML = answer[i].split(',')[1];
    var section = document.createElement('section');
    section.classList.add('p-accordion__panel');
    section.setAttribute('aria-hidden', true);
    section.append(question_title);
    section.append(question_p);
    section.append(answer_title);
    section.append(answer_p);
    li.append(button);
    li.append(section);
    answers.append(li);
  });
}

var toggle_answer = function(e) {
  let parent = e.parentElement;
  let answer_section = parent.lastChild;
  answer_section.setAttribute(
    'aria-hidden',
    (answer_section.getAttribute('aria-hidden')) == "false" ? true : false
  );
}

// load settings
pipelines().then(data => {
  const {dataset, algorithm, domain_limit} = data;
  fill_settings('dataset', dataset);
  fill_settings('algorithm', algorithm);
  fill_settings('domain_limit', domain_limit);
});

// empty questions
document.querySelector('#question').value = '';
