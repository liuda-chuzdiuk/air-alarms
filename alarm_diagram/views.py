import requests

from django.shortcuts import render

from alarm_diagram.models import State, Alarm


def index(request):
    """View function for the home page of the app, which show alarm statistic"""

    headers = {"X-API-Key": "8abab085f6568af9c5415ceec554762ede82f097"}
    url_states = "https://alerts.com.ua/api/states"
    url_history = "https://alerts.com.ua/api/history"
    states_response = requests.get(url=url_states, headers=headers)
    history_response = requests.get(url=url_history, headers=headers)

    start_date = history_response.json()[0]["date"][:10]
    end_date = history_response.json()[-1]["date"][:10]

    # for raw in states_response.json()["states"]:
    #     state = State.objects.get_or_create(
    #         state_id=raw["id"],
    #         name=raw["name"],
    #         name_en=raw["name_en"]
    #     )[0]
    #     state.alarms_count = 0
    #     state.save()
    #
    # for raw in history_response.json():
    #     if raw["alert"]:
    #         alarm = Alarm.objects.get_or_create(
    #             id=raw["id"],
    #             state_id_id=raw["state_id"],
    #             alert=raw["alert"],
    #         )
    #         state = State.objects.get(state_id=alarm[0].state_id_id)
    #         state.alarms_count += 1
    #         state.save()

    states = State.objects.all().order_by("alarms_count")

    context = {
        "states": states,
        "start_date": start_date,
        "end_date": end_date
    }

    return render(request, "index.html", context=context)
