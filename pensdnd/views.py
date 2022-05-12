from django.shortcuts import render
from django.views.generic import TemplateView

class HomePageView(TemplateView):
	template_name = "static/html/index.html"

class BeADM(TemplateView):
	template_name = "static/html/be_a_dm.html"

class GuildRules(TemplateView):
	template_name = "static/html/guild_rules.html"

class CommunityRules(TemplateView):
	template_name = "static/html/community_rules.html"

class ArvonRules(TemplateView):
	template_name = "static/html/arvon_rules.html"

class Volunteer(TemplateView):
	template_name = "static/html/volunteer.html"

class HowToDemo(TemplateView):
	template_name = "static/html/how_to_play_demo.html"
