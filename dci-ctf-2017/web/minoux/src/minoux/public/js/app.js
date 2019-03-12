var e = React.createElement;

var IndexPage = React.createClass({
    getInitialState: function() {
        return {
            roomName: ''
        };
    },

    handleChange: function (evt) {
        this.setState({ roomName: evt.target.value });
    },

    render: function() {
        return e('div', null, [
            e('div', { className: 'lead' }, [
                e('h2', null, "Welcome to Minoux"),
                e('p', null, "Minoux will change the world of online communication by providing an open chat platform that doesn't suck."),
                e('p', null, "This is still very alpha so don't break anything please. We have someone that watches the databases.")
            ]),

            e('input', { onChange: this.handleChange, onKeyPress: this.handleChange, value: this.state.roomName }, null),
            e('button', { onClick: () => this.props.onRoomChange(this.state.roomName) }, 'Join')
        ]);
    }

});

var RoomPage = React.createClass({
    getInitialState: function() {
        return {
            message: ''
        };
    },

    handleChange: function (evt) {
        this.setState({ message: evt.target.value });
    },

    handleSend: function() {
        this.props.sendMessage(this.state.message);
        this.setState({ message: '' });
    },

    render: function() {
        return e('div', null, [
            e('h2', null, this.props.name),
            e('div', { className: 'messages' }, this.props.messages.map((message) => e('div', null, message))),

            e('div', null, [
                e('input', { onChange: this.handleChange, value: this.state.message }, null),
                e('button', { onClick: this.handleSend }, 'Send')
            ])

        ]);
    }
});


var App = React.createClass({
    getInitialState: function() {
        return {
            username: 'anonymous',
            page: 'index',
            rooms: ['general', 'random'],
            status: false,
            messages: {}
        };
    },

    componentDidMount: function() {
        this.ws = new WebSocket('ws://' + location.host);

        this.ws.onopen = () => {
            this.setState({ status: true });
        };

        this.ws.onclose = () => {
            this.setState({ status: false });
        };

        this.ws.onmessage = (msg) => {
            var parser = new protocol(msg.data);
            var data = parser.parse();

            if(typeof data == 'number') {
                if(data === 0) {
                    alert("An error occured while publishing your message. Make sure someone have not already said the same thing in this room. PS: I'm watching you.");
                } else {
                    this.loadRoom(this.state.page.slice(1));
                }
            } else {
                if(this.state.page[0] == '#') {
                    this.state.messages[this.state.page.slice(1)] = data.map((x) => {
                        try {
                            return atob(x);
                        } catch(e) {
                            return '';
                        }
                    });

                    this.setState({ messages: this.state.messages });
                }
            }
        };
    },

    handleRoomClick: function(room) {
        if(this.state.page == `#${room}`) {
            var rooms = this.state.rooms;
            rooms.splice(rooms.indexOf(room), 1);

            this.setState({ rooms: rooms, page: 'index' });
        } else {
            this.setState({ page: `#${room}` });

            if(!this.state.messages[room]) {
                this.loadRoom(room);
            }
        }
    },

    handleRoomChange: function(room) {
        this.setState({ rooms: this.state.rooms.concat(room) });
    },

    loadRoom: function(room) {
        this.ws.send(JSON.stringify({ type: 'messages', room: room }));
    },

    sendMessage: function(message) {
        this.ws.send(JSON.stringify({
            type: 'publish',
            room: this.state.page.slice(1),
            data: btoa(message)
        }));
    },

    render: function() {
        var links = [e('a', { onClick: () => this.setState({ page: 'index' }),
                              href: '#index',
                              className: this.state.page == 'index' ? 'selected' : '' },
                       'Home')
                    ].concat(this.state.rooms.map((room) => e('a', { onClick: this.handleRoomClick.bind(this, room),
                                                                     href:'##' + room,
                                                                     className: this.state.page == `#${room}` ? 'selected room' : 'room' },
                                                              `${room}`) ));
        var currentPage;

        if(this.state.page == 'index') {
            currentPage = e(IndexPage, {
                onRoomChange: this.handleRoomChange
            }, null);
        } else {
            currentPage = e(RoomPage, {
                name: this.state.page,
                messages: this.state.messages[this.state.page.slice(1)] || [],
                sendMessage: this.sendMessage
            }, null);
        }

        return e('div', null, [
            e('div', { className: 'left' }, [
                e('h1', null, 'Minoux'),
                e('nav', null, links),
                e('p', null, this.state.status ? 'Connected' : 'Disconnected'),
            ]),

            e('div', { className: 'right' }, [
                currentPage
            ])
        ]);
    }
});
