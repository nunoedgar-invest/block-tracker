def delete_related_obj(base_object):
    for relationship in base_object._meta.related_objects:
        model = relationship.related_model
        query_filter = {
            relationship.remote_field.name: base_object,
        }

        if relationship.one_to_many or relationship.one_to_one:
            for related_object in model.objects.filter(**query_filter).all():
                delete_related_obj(related_object)
                related_object.delete()
