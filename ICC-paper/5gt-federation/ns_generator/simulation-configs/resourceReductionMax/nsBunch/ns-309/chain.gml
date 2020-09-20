graph [
  node [
    id 0
    label 1
    disk 9
    cpu 1
    memory 14
  ]
  node [
    id 1
    label 2
    disk 3
    cpu 1
    memory 10
  ]
  node [
    id 2
    label 3
    disk 2
    cpu 1
    memory 5
  ]
  node [
    id 3
    label 4
    disk 2
    cpu 2
    memory 9
  ]
  node [
    id 4
    label 5
    disk 8
    cpu 4
    memory 1
  ]
  node [
    id 5
    label 6
    disk 8
    cpu 2
    memory 12
  ]
  node [
    id 6
    label "start"
  ]
  edge [
    source 0
    target 6
    delay 26
    bw 101
  ]
  edge [
    source 0
    target 1
    delay 31
    bw 155
  ]
  edge [
    source 0
    target 2
    delay 31
    bw 157
  ]
  edge [
    source 0
    target 3
    delay 27
    bw 149
  ]
  edge [
    source 1
    target 4
    delay 27
    bw 137
  ]
  edge [
    source 3
    target 5
    delay 28
    bw 136
  ]
]
