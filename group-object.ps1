


function Group-ObjectStaged
{
    <#
        I made this function as the built in group object did not work the way
        I needed for CSV reduction via nested groupping convertto-json
    #>
    param(
        [parameter()]
        [object[]]$inputObject,
        [parameter()]
        [String[]]$Properties
    )
    <# define our return object #>
    $ret = @{}
    <# get our first property #>
    $firstProperty=$Properties | Select -First 1
    <# if no propertyies passed return input we were given #>
    if (-not $firstProperty){
        return $inputObject
    }
    <# else filter input object by first property unique #>
    $interumObject = $inputObject | Sort-Object -Property $firstProperty -Unique

    <# iter through each of the property name and create a dictionary entry if property does not exist #>
    forEach($obj in $interumObject) {
        if ($obj.$firstProperty -notin $ret) {
            $ret.Add($obj.$firstProperty, $null)
        }
        <# 
            filter the input objects property that match the current name we are working on
            remove the property name after filter
         #>
        $passObject = ($inputObject | Where {$_.$firstProperty -eq $obj.$firstProperty} | Select * -ExcludeProperty "$($firstProperty)")
        <#
            Assign the key value to the result of a self call with filter reduction
        #>
        $ret."$($obj.$firstProperty)" = Group-ObjectStaged -inputObject $passObject -Properties ($Properties | Select -Skip 1)

    }
    return $ret
}

