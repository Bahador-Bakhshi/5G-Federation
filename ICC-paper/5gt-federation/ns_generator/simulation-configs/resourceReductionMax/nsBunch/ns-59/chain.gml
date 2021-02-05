graph [
  node [
    id 0
    label 1
    disk 4
    cpu 3
    memory 14
  ]
  node [
    id 1
    label 2
    disk 10
    cpu 3
    memory 3
  ]
  node [
    id 2
    label 3
    disk 2
    cpu 4
    memory 13
  ]
  node [
    id 3
    label 4
    disk 9
    cpu 4
    memory 4
  ]
  node [
    id 4
    label 5
    disk 1
    cpu 3
    memory 2
  ]
  node [
    id 5
    label 6
    disk 2
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
    bw 192
  ]
  edge [
    source 0
    target 1
    delay 35
    bw 105
  ]
  edge [
    source 1
    target 2
    delay 25
    bw 68
  ]
  edge [
    source 2
    target 3
    delay 33
    bw 81
  ]
  edge [
    source 3
    target 4
    delay 25
    bw 165
  ]
  edge [
    source 4
    target 5
    delay 34
    bw 123
  ]
]
