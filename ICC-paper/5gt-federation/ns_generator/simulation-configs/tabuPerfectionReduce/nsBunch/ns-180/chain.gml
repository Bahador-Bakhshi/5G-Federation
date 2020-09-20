graph [
  node [
    id 0
    label 1
    disk 3
    cpu 3
    memory 10
  ]
  node [
    id 1
    label 2
    disk 7
    cpu 2
    memory 5
  ]
  node [
    id 2
    label 3
    disk 6
    cpu 1
    memory 6
  ]
  node [
    id 3
    label 4
    disk 10
    cpu 1
    memory 7
  ]
  node [
    id 4
    label 5
    disk 4
    cpu 2
    memory 7
  ]
  node [
    id 5
    label 6
    disk 9
    cpu 1
    memory 14
  ]
  node [
    id 6
    label "start"
  ]
  edge [
    source 0
    target 6
    delay 35
    bw 148
  ]
  edge [
    source 0
    target 1
    delay 25
    bw 195
  ]
  edge [
    source 0
    target 2
    delay 28
    bw 192
  ]
  edge [
    source 0
    target 3
    delay 30
    bw 169
  ]
  edge [
    source 1
    target 4
    delay 26
    bw 145
  ]
  edge [
    source 2
    target 4
    delay 25
    bw 123
  ]
  edge [
    source 3
    target 4
    delay 35
    bw 161
  ]
  edge [
    source 4
    target 5
    delay 27
    bw 57
  ]
]
