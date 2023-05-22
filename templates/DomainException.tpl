<?php

declare(strict_types=1);

namespace App\Domain\##TABLENAME##;

use App\Domain\DomainException\DomainRecordNotFoundException;

class ##TABLENAME##NotFoundException extends DomainRecordNotFoundException
{
    public $message = 'Unable to find the requested record into the entity ##TABLENAME##.';
}
