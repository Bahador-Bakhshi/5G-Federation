graph [
  node [
    id 0
    label 1
    disk 6
    cpu 2
    memory 7
  ]
  node [
    id 1
    label 2
    disk 2
    cpu 1
    memory 10
  ]
  node [
    id 2
    label 3
    disk 5
    cpu 4
    memory 4
  ]
  node [
    id 3
    label 4
    disk 6
    cpu 2
    memory 10
  ]
  node [
    id 4
    label 5
    disk 9
    cpu 2
    memory 14
  ]
  node [
    id 5
    label 6
    disk 10
    cpu 3
    memory 10
  ]
  node [
    id 6
    label "start"
  ]
  edge [
    source 0
    target 6
    delay 34
    bw 120
  ]
  edge [
    source 0
    target 1
    delay 29
    bw 81
  ]
  edge [
    source 0
    target 2
    delay 31
    bw 145
  ]
  edge [
    source 0
    target 3
    delay 30
    bw 119
  ]
  edge [
    source 1
    target 4
    delay 34
    bw 92
  ]
  edge [
    source 2
    target 5
    delay 33
    bw 166
  ]
  edge [
    source 3
    target 4
    delay 33
    bw 155
  ]
]
