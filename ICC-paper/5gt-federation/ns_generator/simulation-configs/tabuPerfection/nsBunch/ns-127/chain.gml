graph [
  node [
    id 0
    label 1
    disk 9
    cpu 1
    memory 10
  ]
  node [
    id 1
    label 2
    disk 7
    cpu 4
    memory 7
  ]
  node [
    id 2
    label 3
    disk 3
    cpu 2
    memory 7
  ]
  node [
    id 3
    label 4
    disk 4
    cpu 4
    memory 6
  ]
  node [
    id 4
    label 5
    disk 7
    cpu 1
    memory 4
  ]
  node [
    id 5
    label 6
    disk 1
    cpu 1
    memory 15
  ]
  node [
    id 6
    label "start"
  ]
  edge [
    source 0
    target 6
    delay 29
    bw 167
  ]
  edge [
    source 0
    target 1
    delay 28
    bw 121
  ]
  edge [
    source 0
    target 2
    delay 27
    bw 165
  ]
  edge [
    source 1
    target 3
    delay 33
    bw 172
  ]
  edge [
    source 2
    target 5
    delay 30
    bw 134
  ]
  edge [
    source 3
    target 4
    delay 33
    bw 108
  ]
  edge [
    source 4
    target 5
    delay 30
    bw 125
  ]
]
