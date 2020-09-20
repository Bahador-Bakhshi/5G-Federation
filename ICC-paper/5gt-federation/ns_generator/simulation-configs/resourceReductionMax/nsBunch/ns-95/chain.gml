graph [
  node [
    id 0
    label 1
    disk 5
    cpu 4
    memory 7
  ]
  node [
    id 1
    label 2
    disk 5
    cpu 3
    memory 3
  ]
  node [
    id 2
    label 3
    disk 5
    cpu 3
    memory 9
  ]
  node [
    id 3
    label 4
    disk 6
    cpu 3
    memory 1
  ]
  node [
    id 4
    label 5
    disk 8
    cpu 2
    memory 16
  ]
  node [
    id 5
    label 6
    disk 10
    cpu 3
    memory 11
  ]
  node [
    id 6
    label "start"
  ]
  edge [
    source 0
    target 6
    delay 35
    bw 115
  ]
  edge [
    source 0
    target 1
    delay 33
    bw 83
  ]
  edge [
    source 0
    target 2
    delay 35
    bw 144
  ]
  edge [
    source 1
    target 3
    delay 35
    bw 151
  ]
  edge [
    source 2
    target 3
    delay 25
    bw 55
  ]
  edge [
    source 3
    target 4
    delay 35
    bw 98
  ]
  edge [
    source 4
    target 5
    delay 26
    bw 145
  ]
]
