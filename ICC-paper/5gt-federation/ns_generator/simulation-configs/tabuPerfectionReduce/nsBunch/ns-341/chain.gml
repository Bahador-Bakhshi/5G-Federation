graph [
  node [
    id 0
    label 1
    disk 1
    cpu 4
    memory 10
  ]
  node [
    id 1
    label 2
    disk 3
    cpu 2
    memory 3
  ]
  node [
    id 2
    label 3
    disk 5
    cpu 2
    memory 9
  ]
  node [
    id 3
    label 4
    disk 3
    cpu 2
    memory 16
  ]
  node [
    id 4
    label 5
    disk 4
    cpu 4
    memory 1
  ]
  node [
    id 5
    label 6
    disk 3
    cpu 1
    memory 1
  ]
  node [
    id 6
    label "start"
  ]
  edge [
    source 0
    target 6
    delay 32
    bw 145
  ]
  edge [
    source 0
    target 1
    delay 32
    bw 96
  ]
  edge [
    source 1
    target 2
    delay 33
    bw 88
  ]
  edge [
    source 1
    target 3
    delay 35
    bw 193
  ]
  edge [
    source 1
    target 4
    delay 25
    bw 139
  ]
  edge [
    source 2
    target 5
    delay 34
    bw 105
  ]
  edge [
    source 3
    target 5
    delay 32
    bw 71
  ]
  edge [
    source 4
    target 5
    delay 25
    bw 50
  ]
]
