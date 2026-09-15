FROM apache/superset:latest

USER root
RUN pip install --target /tmp/psycopg2 psycopg2-binary && \
    cp -r /tmp/psycopg2/psycopg2* /app/.venv/lib/python3.10/site-packages/ && \
    rm -rf /tmp/psycopg2 && \
    python -c "from babel.messages.mofile import write_mo; from babel.messages.pofile import read_po; \
    catalog = read_po(open('/app/superset/translations/pt_BR/LC_MESSAGES/messages.po','rb')); \
    write_mo(open('/app/superset/translations/pt_BR/LC_MESSAGES/messages.mo','wb'), catalog)"
USER superset
