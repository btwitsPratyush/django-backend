from django.contrib import admin
from django.utils.html import format_html
from .models import PayoutRequest

@admin.register(PayoutRequest)
class PayoutRequestAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'amount', 'recipient_account', 'colored_status', 'created_at')
    list_filter = ('status', 'created_at')
    search_fields = ('user__username', 'recipient_account')
    readonly_fields = ('created_at',)
    actions = ['mark_as_success', 'mark_as_failed', 'export_as_csv']

    def colored_status(self, obj):
        color = {
            'PENDING': 'orange',
            'SUCCESS': 'green',
            'FAILED': 'red'
        }.get(obj.status, 'black')
        return format_html('<strong style="color: {};">{}</strong>', color, obj.status)
    colored_status.short_description = 'Status'

    def mark_as_success(self, request, queryset):
        updated = queryset.update(status='SUCCESS')
        self.message_user(request, f"{updated} payout(s) marked as SUCCESS.")
    mark_as_success.short_description = "Mark selected payouts as SUCCESS"

    def mark_as_failed(self, request, queryset):
        updated = queryset.update(status='FAILED')
        self.message_user(request, f"{updated} payout(s) marked as FAILED.")
    mark_as_failed.short_description = "Mark selected payouts as FAILED"

    def export_as_csv(self, request, queryset):
        import csv
        from django.http import HttpResponse

        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename="payout_requests.csv"'

        writer = csv.writer(response)
        writer.writerow(['ID', 'User', 'Amount', 'Recipient Account', 'Status', 'Created At'])
        for obj in queryset:
            writer.writerow([obj.id, obj.user.username, obj.amount, obj.recipient_account, obj.status, obj.created_at])

        return response
    export_as_csv.short_description = "Export selected payouts as CSV"
