#!/bin/bash
export AUTH0_DOMAIN='doc-nano.us.auth0.com'
export ALGORITHMS=['RS256']
export API_AUDIENCE='doc-capstone'
export CLIENT_ID='7hPGqquzuZyGqY8eZVmFPXOxwonXTKYJ'
export FLASK_APP=app.py
export DATABASE_URL=postgresql://postgres@localhost:5432
export DIRECTOR_TOKEN='eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6Imp6Y0dxVVJIeWlZdGRvSTdWMWI0SSJ9.eyJpc3MiOiJodHRwczovL2RvYy1uYW5vLnVzLmF1dGgwLmNvbS8iLCJzdWIiOiJhdXRoMHw2NGU5NTdiMjc2OGQ0NzZlMzgyMTA3MTgiLCJhdWQiOiJkb2MtY2Fwc3RvbmUiLCJpYXQiOjE2OTY3MTUyNTAsImV4cCI6MTY5NjcyMjQ1MCwiYXpwIjoidlU5alZrWlZxVzBkWkZGSkloMlIyamc1NHJDUlpBV1oiLCJzY29wZSI6IiIsInBlcm1pc3Npb25zIjpbImFkZDphY3RvciIsImRlbGV0ZTphY3RvciIsImdldDphY3RvcnMiLCJnZXQ6bW92aWVzIiwidXBkYXRlOmFjdG9yIiwidXBkYXRlOm1vdmllIl19.EMTZhAXAoKc_7DLpW_4TzCDxaxwNF3rQx8elIWBJ5cUyanrkJufRA3XLx7BKl2rf76wFZcYDmfuDmo6qUvK7VFH1leyTVACu-6dSdb0Dg6HSGZPuMsmWdZK1o_ZlKpKXwqehX8PeQccmT3DHj34UABzWS8ySO8UQq2UbTBgLANU7gFKGaGabuGu8rAe45UDauoBXVdHcGF123h8FaOAdJXsMPDsifZxo4NLrTbSQpqnBYjEiIjsTIlck4o1FPZ8Uf5lBjtuaXgjz_iHPjjnRkCZkvpd-3kFsPdX86GIu3eK10dHA3w1P2vyMlIdbZQ6Nk4JxotnUVeAUE4tWtXf5VQ'
export PRODUCER_TOKEN='eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6Imp6Y0dxVVJIeWlZdGRvSTdWMWI0SSJ9.eyJpc3MiOiJodHRwczovL2RvYy1uYW5vLnVzLmF1dGgwLmNvbS8iLCJzdWIiOiJhdXRoMHw2NGU5NTdlNDQ5OGVlMWVlMzE3ZmJkMGIiLCJhdWQiOiJkb2MtY2Fwc3RvbmUiLCJpYXQiOjE2OTY3MTQxNDQsImV4cCI6MTY5NjcyMTM0NCwiYXpwIjoidlU5alZrWlZxVzBkWkZGSkloMlIyamc1NHJDUlpBV1oiLCJzY29wZSI6IiIsInBlcm1pc3Npb25zIjpbImFkZDphY3RvciIsImFkZDptb3ZpZSIsImRlbGV0ZTphY3RvciIsImRlbGV0ZTptb3ZpZSIsImdldDphY3RvcnMiLCJnZXQ6bW92aWVzIiwidXBkYXRlOmFjdG9yIiwidXBkYXRlOm1vdmllIl19.Gix1qfuqLVrMALO5GWcnWX_LCX48qwXO68kRlUAzMvF86NIgFAs57ncvFMuYtEy4u89HhCDqaoRuFssMe-NdMN70LIPXTMuY4nQMS7dlrVRbZqFcctqtBIvLsUEB9iHmk2TXRLVV2_SMdCpAn8T_OpioCy9i2NzLzNpyM-4YohsZFQNi734JcwH7sg69IeXUe226LJH7rKmeEj440MYHjxSJvJeoefvrFvzSdGcK41_EC6IfP-qYc9plMMDn8HReCc25A8AZK57z0SI_yGh2RsGZZSN9O9zWE9_wSepn5g1Vv8XIM5347aiN9pKQVh6ahtj5731ZBEBDiU3yYFOEcg'
export ASSISTANT_TOKEN='eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6Imp6Y0dxVVJIeWlZdGRvSTdWMWI0SSJ9.eyJpc3MiOiJodHRwczovL2RvYy1uYW5vLnVzLmF1dGgwLmNvbS8iLCJzdWIiOiJhdXRoMHw2NGU5NTc5MzA4NmY5MGRhMTQyNjBjNjYiLCJhdWQiOiJkb2MtY2Fwc3RvbmUiLCJpYXQiOjE2OTY3MTUyMDYsImV4cCI6MTY5NjcyMjQwNiwiYXpwIjoidlU5alZrWlZxVzBkWkZGSkloMlIyamc1NHJDUlpBV1oiLCJzY29wZSI6IiIsInBlcm1pc3Npb25zIjpbImdldDphY3RvcnMiLCJnZXQ6bW92aWVzIl19.jVbxKeilRtnprirPaZ8BqTWls-L15rYgoESRdsNxuPTSKiY7UqqYqQCfPaVaHJd7gVE0ilObDYvGaVok0Pv1z5ihYU6JX57wMBjtGQWqz8LO5wRuhqv2Fz7RNe4YBClTvVICDeZUDRyfcGigUY5fPHsQBET39lIkz7ve0Kk0cms2BgSkJkrykKIm-mpy-EwvGBN9izDdmL64u-L8yOIf0NFGMKsG76geVuj_kXhB98f1tKDDCgKcF9_pvt7PcnQdbgNxs1YbX7x3fpHfSi2FtyNjCt8aSp49CcYReT053FciDWxS-Ma2ZIenpnxbf-STdW87NsPRh5yZ34OrS0SlTA'
# https://doc-nano.us.auth0.com/authorize?audience=doc-capstone&response_type=token&client_id=vU9jVkZVqW0dZFFJIh2R2jg54rCRZAWZ&redirect_uri=http://127.0.0.1:8080/