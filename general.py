import os
from flask_migrate import Migrate
from app import blueprint
from app.main import create_app, db
from app.main.model import orderline, order
from app.main.service import orderline_service

# app = create_app(os.getenv('BOILERPLATE_ENV') or 'dev')

#
# @app.route('/')
# def main():
#     return orderline_service.get_all_orderlines()
#
#
# if __name__ == "__main__":
#     app.run(host="0.0.0.0", port=8080, debug=True, use_reloader=True)
#
# app.register_blueprint(blueprint)
#
# app.app_context().push()
#
# migrate = Migrate(app, db)

@app.shell_context_processor
def make_shell_context():
    return dict(db=db, Orderline=orderline, Order=order)



# Easy DB creation

# create table main.orderline
# (
#     id                     integer not null
#         constraint orderline_pk
#             primary key autoincrement,
#     brand_id               integer not null,
#     contractual_partner_id integer,
#     completed              boolean default FALSE
# );

# create table main."order"
# (
#     id                     integer
#         constraint order_pk
#             primary key autoincrement,
#     order_code             string(15)            not null,
#     orderline_id           integer               not null,
#     orderline_pos          integer               not null,
#     style_number           integer               not null,
#     brand_id               integer               not null,
#     contractual_partner_id integer               not null,
#     completed              boolean default false not null,
#     final_client_id        integer               not null
# );

# create table main.task
# (
#     id          integer    not null
#         constraint task_pk
#             primary key autoincrement,
#     date_issued DateTime   not null,
#     status      string(10) not null,
#     evidence_id integer    not null,
#     task_type   string(25) not null,
#     order_code  string(25) not null
# );

# TODO: add step query