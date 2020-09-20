graph [
  node [
    id 0
    label 1
    disk 1
    cpu 4
    memory 4
  ]
  node [
    id 1
    label 2
    disk 8
    cpu 1
    memory 13
  ]
  node [
    id 2
    label 3
    disk 7
    cpu 3
    memory 3
  ]
  node [
    id 3
    label 4
    disk 6
    cpu 4
    memory 16
  ]
  node [
    id 4
    label 5
    disk 6
    cpu 2
    memory 2
  ]
  node [
    id 5
    label 6
    disk 10
    cpu 1
    memory 3
  ]
  node [
    id 6
    label "start"
  ]
  edge [
    source 0
    target 6
    delay 32
    bw 67
  ]
  edge [
    source 0
    target 1
    delay 35
    bw 149
  ]
  edge [
    source 0
    target 2
    delay 25
    bw 155
  ]
  edge [
    source 1
    target 3
    delay 26
    bw 135
  ]
  edge [
    source 2
    target 4
    delay 34
    bw 148
  ]
  edge [
    source 3
    target 5
    delay 33
    bw 71
  ]
  edge [
    source 4
    target 5
    delay 32
    bw 97
  ]
]
