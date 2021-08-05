
create table products (
    id           integer primary key autoincrement not null,
    name         text,
    price        integer,
    description   text,
    picture      text
);


insert into products (name, price, description, picture)
        values ('Python Cat of the Week', 12, "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Pellentesque molestie diam vel pretium pharetra. Donec neque est, elementum ut diam ut, facilisis lobortis nulla. In a turpis magna. Suspendisse ut enim gravida, sollicitudin quam in, placerat tortor. Suspendisse sodales et odio egestas placerat. Cras tempor volutpat ex id elementum. Pellentesque varius hendrerit rhoncus. Nunc auctor ut purus sit amet facilisis. Ut magna sapien, convallis vitae molestie ac, scelerisque et tellus. Ut a quam mauris. In hac habitasse platea dictumst.", 'https://picsum.photos/id/237/200');

insert into products (name, price, description, picture)
        values ('Python Dog of the Week', 32, "Nam scelerisque tincidunt lectus a viverra. Cras porta lobortis ipsum a luctus. Aliquam eu volutpat purus. Integer dui magna, feugiat ut porttitor non, cursus eu odio. Curabitur pharetra luctus sodales. Sed at malesuada nisl, vel auctor diam. Nunc turpis tellus, malesuada id lacinia non, lacinia condimentum magna. Pellentesque non erat nibh. Pellentesque venenatis ipsum a quam suscipit sagittis. In hac habitasse platea dictumst. Donec enim neque, ullamcorper eget dolor ut, interdum tristique orci.", 'https://picsum.photos/id/239/200');
insert into products (name, price, description, picture)
        values ('Python Snake of the Week', 55, "Vivamus sed porta nisl. Mauris commodo venenatis lorem fermentum laoreet. Donec in diam ac ex sodales venenatis. In ultricies, nunc et maximus tempor, magna tortor ultrices nisl, ut laoreet nisi massa eget ex. Mauris tristique justo eget erat tempus aliquam. Aenean rutrum lectus sed gravida fringilla. Mauris in sem sit amet erat porta sodales. Ut laoreet ut massa at fermentum. Duis vulputate, nibh id semper convallis, diam est varius turpis, nec accumsan diam dolor id est. Nullam cursus elit quis eros sodales, at sollicitudin odio commodo. Phasellus rhoncus mauris sed fringilla scelerisque. Ut augue nisi, sodales eu dolor ut, elementum blandit mi. Donec molestie malesuada sollicitudin.", 'https://picsum.photos/id/238/200');
insert into products (name, price, description, picture)
        values ('Python Mouse of the Week', 33, "Duis hendrerit semper luctus. Nunc fringilla sit amet dolor vitae imperdiet. Proin ac felis nec quam blandit tempor ac non ex. In hac habitasse platea dictumst. Proin ultrices ullamcorper elementum. Aenean massa mi, aliquet sit amet arcu fringilla, pellentesque pretium justo. Suspendisse eget urna malesuada, tristique mi sed, tincidunt enim. Nunc sed odio neque. Vivamus in eros volutpat justo interdum finibus ut at ipsum. Maecenas ut purus in magna rhoncus pulvinar. Donec non faucibus libero, vel consectetur urna. Fusce eu turpis sed risus venenatis posuere.", 'https://picsum.photos/id/1003/200');
insert into products (name, price, description, picture)
        values ('Python Pig of the Week', 77, "Curabitur blandit eros sed lacus fermentum, nec laoreet leo malesuada. Ut faucibus porttitor consequat. Integer nisl velit, blandit sit amet efficitur eget, porta sed lectus. Curabitur finibus in magna vitae consectetur. Vestibulum maximus orci elementum metus sodales vehicula. Donec et purus vestibulum, euismod metus eget, volutpat nisl. Nulla pulvinar convallis fringilla. Pellentesque sed consectetur libero. Nunc dapibus accumsan mi, a consectetur lacus consectetur et. Phasellus vitae orci sit amet massa pulvinar pulvinar ut et dui. Morbi magna ante, sodales sit amet nulla porta, eleifend ullamcorper dui.", 'https://picsum.photos/200');
