from rest_framework import serializers
from .models import Company, Vacancy

class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = '__all__'

class VacancySerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=255)
    description = serializers.CharField()
    salary = serializers.DecimalField(max_digits=10, decimal_places=2)
    company = CompanySerializer(read_only=True)
    company_id = serializers.IntegerField(write_only=True)

    def create(self, validated_data):
      
        company_id = validated_data.pop('company_id')
        company = Company.objects.get(id=company_id) 
        vacancy = Vacancy.objects.create(company=company, **validated_data)
        return vacancy

    def update(self, instance, validated_data):
       
        if 'company_id' in validated_data:
            company_id = validated_data.pop('company_id')
            instance.company = Company.objects.get(id=company_id)
       
        instance.name = validated_data.get('name', instance.name)
        instance.description = validated_data.get('description', instance.description)
        instance.salary = validated_data.get('salary', instance.salary)
        
        instance.save()
        return instance