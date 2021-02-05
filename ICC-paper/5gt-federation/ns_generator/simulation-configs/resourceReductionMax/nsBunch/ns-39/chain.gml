graph [
  node [
    id 0
    label 1
    disk 6
    cpu 1
    memory 3
  ]
  node [
    id 1
    label 2
    disk 9
    cpu 2
    memory 16
  ]
  node [
    id 2
    label 3
    disk 5
    cpu 1
    memory 15
  ]
  node [
    id 3
    label 4
    disk 7
    cpu 4
    memory 9
  ]
  node [
    id 4
    label 5
    disk 7
    cpu 4
    memory 12
  ]
  node [
    id 5
    label 6
    disk 10
    cpu 4
    memory 3
  ]
  node [
    id 6
    label "start"
  ]
  edge [
    source 0
    target 6
    delay 35
    bw 117
  ]
  edge [
    source 0
    target 1
    delay 31
    bw 124
  ]
  edge [
    source 0
    target 2
    delay 28
    bw 182
  ]
  edge [
    source 0
    target 3
    delay 25
    bw 92
  ]
  edge [
    source 1
    target 5
    delay 29
    bw 139
  ]
  edge [
    source 3
    target 4
    delay 29
    bw 60
  ]
]
