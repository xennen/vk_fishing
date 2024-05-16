import vk
from typing import List, Optional
from datetime import datetime, date
import csv
from connections.connection_manager import ConnectionManager
from .model import Members
from logging import Logger


class FromVkToCsv():
    def __init__(self, api: vk.API, csv_file_path: str, group_id: str, logger: Logger) -> None:
        self.api = api
        self.csv_file_path = csv_file_path
        self.group_id = group_id
        self.logger = logger
        self.headers = ["user_id_vk", "fullname",
                        "last_seen", "contacts", "friends_count", "town", "age"]
        self.additional_fields = ['city', 'contacts', 'last_seen', 'bdate']

    # Получаем пользователей
    def get_members(self, group_id: str, fields: List, fil="") -> List:
        return self.api.groups.getMembers(group_id=group_id, sort='id_asc', filter=fil, fields=fields)

    # Получаем количество друзей
    def get_friends_count(self, user_id) -> int:
        return len(self.api.friends.get(user_id=user_id)['items'])

    # Проверяем открыт ли профиль для счета друзей
    def friends_count(self, member) -> int:
        count = 0
        if not member['is_closed']:
            count = self.get_friends_count(member['id'])
        return count

    # Получаем последний визит
    def get_last_seen(self, member) -> Optional[datetime]:
        last_seen = None
        if 'last_seen' in member:
            last_seen = datetime.fromtimestamp(
                member['last_seen']['time']).strftime('%Y-%m-%d %H:%M:%S')
            return last_seen

    # Получаем контакт если есть
    def get_mobile_phone(self, member) -> str:
        mobile_phone = ''
        if 'mobile_phone' in member:
            mobile_phone = member['mobile_phone']
        return mobile_phone

    # Получаем город если есть
    def get_town(self, member) -> str:
        town = ''
        if 'city' in member:
            town = member['city']['title']
        return town

    # Получаем возраст если указана корректная дата рождения
    def get_age(self, member) -> Optional[int]:
        age = None
        if 'bdate' in member:
            try:
                age = date.today().year - datetime.strptime(member['bdate'], '%d.%m.%Y').year
            except Exception as err:
                self.logger.info(f'ERROR {err}')
            
            finally: 
                return age

    # Записываем в csv пользователей
    def members_to_scv(self) -> None:
        with open(self.csv_file_path, mode="w", newline="", encoding="utf-8") as file:
            writer = csv.DictWriter(
                file, fieldnames=self.headers, delimiter='\t')
            writer.writeheader()

            list_members = self.get_members(
                self.group_id, self.additional_fields)['items']
            for member in list_members:
                if 'deactivated' in member:
                    self.logger.info(
                        f"User {member['id']} get {member['deactivated']}")
                    continue
                friends_count = self.friends_count(member)
                last_seen = self.get_last_seen(member)
                mobile_phone = self.get_mobile_phone(member)
                town = self.get_town(member)
                age = self.get_age(member)
                self.logger.info(f"User {member['id']} added in .csv")

                mem = Members(
                    user_id_vk=member['id'],
                    fullname=' '.join(
                        [member['first_name'], member['last_name']]),
                    last_seen=last_seen,
                    contacts=mobile_phone,
                    friends_count=friends_count,
                    town=town,
                    age=age
                )
                writer.writerow(mem.model_dump())
