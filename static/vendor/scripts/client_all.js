const methods = document.getElementById('methods');
const methodsli = document.querySelector('.methods-li');
const feelings = document.getElementById('feelings');
const feelingsli = document.querySelector('.feelings-li');
const events = document.getElementById('events');
const eventsli = document.querySelector('.events-li');
const time = document.getElementById('time');
const timeli = document.querySelector('.time-li');
const price = document.getElementById('price');
const priceli = document.querySelector('.price-li');
function showMethods() {
  const methods__checkbox = document.querySelectorAll('.methods__checkbox');

  if (methods__checkbox.length === 0) {
    methodsli.insertAdjacentHTML(
      'afterend',
      `<li class="therapists__item methods__checkbox">
    <label for="methods">
      <input
        id="methods"
        name="TherapyMethods"
        value="Психоанализ"
        type="checkbox"
      />
      Психоанализ</label
    >
  </li>
  <li class="therapists__item methods__checkbox">
    <label for="">
      <input
        id=""
        name="Позитивное психотерапия"
        value="Позитивное психотерапия"
        type="checkbox"
      />
      Позитивное психотерапия</label
    >
  </li>
  <li class="therapists__item methods__checkbox">
    <label for="">
      <input
        id=""
        name="Психодрама"
        value="Психодрама"
        type="checkbox"
      />
      Психодрама
    </label>
  </li>
  <li class="therapists__item methods__checkbox">
    <label for="">
      <input
        id=""
        name="Гештальт"
        value="Гештальт"
        type="checkbox"
      />
      Гештальт
    </label>
  </li>
  <li class="therapists__item methods__checkbox">
    <label for="">
      <input
        id=""
        name="Эмоционально-образная"
        value="Эмоционально-образная"
        type="checkbox"
      />
      Эмоционально-образная
    </label>
  </li>
  <li class="therapists__item methods__checkbox">
    <label for="">
      <input
        id=""
        name="Телесная"
        value="Телесная"
        type="checkbox"
      />
      Телесная
    </label>
  </li>
  <li class="therapists__item methods__checkbox">
    <label for="">
      <input
        id=""
        name="Семейная"
        value="Семейная"
        type="checkbox"
      />
      Семейная
    </label>
  </li>
  <li class="therapists__item methods__checkbox">
    <label for="">
      <input
        id=""
        name="Психодинамическая"
        value="Психодинамическая"
        type="checkbox"
      />
      Психодинамическая
    </label>
  </li>
  <li class="therapists__item methods__checkbox">
    <label for="">
      <input
        id=""
        name="Коучинг"
        value="Коучинг"
        type="checkbox"
      />
      Коучинг
    </label>
  </li>
`,
    );
  } else {
    methods__checkbox.forEach((element) => {
      element.remove();
    });
  }
}

function showFeelings() {
  const feelings__checkbox = document.querySelectorAll('.feelings__checkbox');

  if (feelings__checkbox.length === 0) {
    feelingsli.insertAdjacentHTML('afterend', ` <li class="therapists__item feelings__checkbox">
      <label for="">
        <input
          id=""
          name="Тревога, стресс"
          value="Тревога, стресс"
          type="checkbox"
        />
        Тревога, стресс</label
      >
    </li>
    <li class="therapists__item feelings__checkbox">
      <label for="">
        <input
          id=""
          name="Апатия, отсутствие сил, увлечений, целей, смысла"
          value="Апатия, отсутствие сил, увлечений, целей, смысла"
          type="checkbox"
        />
        Апатия, отсутствие сил, увлечений, целей, смысла</label
      >
    </li>
    <li class="therapists__item feelings__checkbox">
      <label for="">
        <input
          id=""
          name="Депрессия"
          value="Депрессия"
          type="checkbox"
        />
        Депрессия</label
      >
    </li>
    <li class="therapists__item feelings__checkbox">
      <label for="">
        <input
          id=""
          name="Зажатость"
          value="Зажатость"
          type="checkbox"
        />
        Зажатость</label
      >
    </li>
    <li class="therapists__item feelings__checkbox">
      <label for="">
        <input
          id=""
          name="Изоляция/ одиночество"
          value="Изоляция/ одиночество"
          type="checkbox"
        />
        Изоляция/ одиночество</label
      >
    </li>
    <li class="therapists__item feelings__checkbox">
      <label for="">
        <input
          id=""
          name="Неудовлетворенность жизнью"
          value="Неудовлетворенность жизнью"
          type="checkbox"
        />
        Неудовлетворенность жизнью</label
      >
    </li>`);
  } else {
    feelings__checkbox.forEach((element) => {
      element.remove();
    });
  }
}
function showEvents() {
  const events__checkbox = document.querySelectorAll('.events__checkbox');

  if (events__checkbox.length === 0) {
    eventsli.insertAdjacentHTML('afterend', `<li class="therapists__item events__checkbox">
    <label for="">
      <input
        id=""
        name="Потеря любимого человека (Развод/расставание)"
        value="Потеря любимого человека (Развод/расставание)"
        type="checkbox"
      />
      Потеря любимого человека (Развод/расставание)</label
    >
  </li>
  <li class="therapists__item events__checkbox">
    <label for="">
      <input
        id=""
        name="Проблемы в семье или отношениях"
        value="Проблемы в семье или отношениях"
        type="checkbox"
      />
      Проблемы в семье или отношениях</label
    >
  </li>
  <li class="therapists__item events__checkbox">
    <label for="">
      <input
        id=""
        name="Проблемы в карьере или учебе"
        value="Проблемы в карьере или учебе"
        type="checkbox"
      />
      Проблемы в карьере или учебе</label
    >
  </li>
  <li class="therapists__item events__checkbox">
    <label for="">
      <input
        id=""
        name="Травма и абьюз"
        value="Травма и абьюз"
        type="checkbox"
      />
      Травма и абьюз</label
    >
  </li>
  <li class="therapists__item events__checkbox">
    <label for="">
      <input
        id=""
        name="Созависимые отношения"
        value="Созависимые отношения"
        type="checkbox"
      />
      Созависимые отношения</label
    >
  </li>`);
  } else {
    events__checkbox.forEach((element) => {
      element.remove();
    });
  }
}
function showTime() {
  const time__checkbox = document.querySelectorAll('.time__checkbox');

  if (time__checkbox.length === 0) {
    timeli.insertAdjacentHTML('afterend', `<li class="therapists__item time__checkbox">
    <label for="">
      <input
        id=""
        name="Ближайшие 24 часа"
        value="Ближайшие 24 часа"
        type="radio"
      />
      Ближайшие 24 часа</label
    >
  </li>
  <li class="therapists__item time__checkbox">
    <label for="">
      <input
        id=""
        name="Ближайшие 3 дня"
        value="Ближайшие 3 дня"
        type="radio"
      />
      Ближайшие 3 дня</label
    >
  </li>
  <li class="therapists__item time__checkbox">
    <label for="">
      <input
        id=""
        name="Ближайшая неделя"
        value="Ближайшая неделя"
        type="radio"
      />
      Ближайшая неделя</label
    >
  </li>
  <li class="therapists__item time__checkbox">
    <label for="">
      <input
        id=""
        name="Ближайший месяц"
        value="Ближайший месяц"
        type="radio"
      />
      Ближайший месяц</label
    >
  </li>
  <li class="therapists__item time__checkbox">
    <label for="">
      <input
        id=""
        name="Не важно"
        value="Не важно"
        type="radio"
      />
      Не важно</label
    >
  </li>`);
  } else {
    time__checkbox.forEach((element) => {
      element.remove();
    });
  }
}

function showPrice() {
  const price__checkbox = document.querySelectorAll('.price__checkbox');

  if (price__checkbox.length === 0) {
    priceli.insertAdjacentHTML('afterend', ` <li class="therapists__item events__checkbox">
    <label for="">
      <input
        id=""
        name="До 3000₽"
        value="До 3000₽"
        type="radio"
      />
      До 3000₽</label
    >
  </li>
  <li class="therapists__item events__checkbox">
    <label for="">
      <input
        id=""
        name="До 5000₽"
        value="До 5000₽"
        type="radio"
      />
      До 5000₽</label
    >
  </li>
  <li class="therapists__item events__checkbox">
    <label for="">
      <input
        id=""
        name="До 8000₽"
        value="До 8000₽"
        type="radio"
      />
      До 8000₽</label
    >
  </li>
  <li class="therapists__item events__checkbox">
    <label for="">
      <input
        id=""
        name="От 8000₽ и более"
        value="От 8000₽ и более"
        type="radio"
      />
      От 8000₽ и более</label
    >
  </li>`);
  } else {
    price__checkbox.forEach((element) => {
      element.remove();
    });
  }
}

methods.addEventListener('click', () => {
  showMethods();
});
feelings.addEventListener('click', () => {
  showFeelings();
});
events.addEventListener('click', () => {
  showEvents();
});
time.addEventListener('click', () => {
  showTime();
});
price.addEventListener('click', () => {
  showPrice();
});
